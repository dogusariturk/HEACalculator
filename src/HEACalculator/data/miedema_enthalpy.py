"""Binary mixing enthalpy from the Miedema macroscopic atom model."""

from __future__ import annotations

import importlib.resources
import json
from bisect import bisect_right
from dataclasses import dataclass

from HEACalculator.data.elements import Element
from HEACalculator.exceptions import MissingMiedemaDataError

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

_data_dir = importlib.resources.files("HEACalculator.data")

with (_data_dir / "model_miedema_params.json").open() as _f:
    _params: dict = json.load(_f)

with (_data_dir / "model_miedema_interfacial.json").open() as _f:
    _interfacial_table: dict[str, dict[str, int]] = json.load(_f)

with (_data_dir / "model_niessen_structural.json").open() as _f:
    _niessen: dict = json.load(_f)

_z_points: list[float] = _niessen["z_points"]
_niessen_energies: dict[str, list[float]] = _niessen["energies_kj_per_mol"]
_reference_structures: dict[int, str] = {int(k): v for k, v in _niessen["reference_structures"].items()}

_ALKALI_METALS = {"Li", "Na", "K", "Rb", "Cs"}
_DIVALENT_METALS = {"Be", "Mg", "Zn", "Cd", "Hg"}
_NOBLE_AND_TRIVALENT_METALS = {"Al", "Ga", "In", "Tl", "Cu", "Ag", "Au", "Sc", "Y", "La"}


def model_niessen_structural() -> dict:
    """Return the structural-enthalpy data derived from Niessen *et al.* (1983).

    Returns:
        Structural energy tables, z-points, and reference structures from the source data.
    """
    return _niessen


def _corrected_volume_term(symbol: str, volume: float, dphi: float, f_ba: float) -> float:
    if symbol in _ALKALI_METALS:
        alpha = 0.14
    elif symbol in _DIVALENT_METALS:
        alpha = 0.10
    elif symbol in _NOBLE_AND_TRIVALENT_METALS:
        alpha = 0.07
    else:
        alpha = 0.04
    return volume ** (2 / 3) * (1 + alpha * f_ba * dphi)


def _elastic_solution_enthalpy(
    solute_symbol: str,
    bulk_solute: float,
    shear_matrix: float,
    volume_solute: float,
    volume_matrix: float,
    phi_solute: float,
    phi_matrix: float,
    n_ws_solute: float,
    n_ws_matrix: float,
    c_matrix_surface: float,
) -> float:
    """Return the directional elastic mismatch enthalpy for a solute in a matrix.

    Returns:
        Elastic mismatch enthalpy in kJ/mol for the supplied solute-matrix direction.
    """
    volume_solute_23 = _corrected_volume_term(solute_symbol, volume_solute, phi_solute - phi_matrix, c_matrix_surface)
    average_n_ws_inv = 0.5 * (n_ws_solute ** (-1 / 3) + n_ws_matrix ** (-1 / 3))
    if average_n_ws_inv == 0:
        return 0.0
    alpha = 3 * volume_solute_23 / (4 * average_n_ws_inv)
    w_solute = volume_solute + alpha * (phi_solute - phi_matrix) / n_ws_solute
    w_matrix = volume_matrix - alpha * (phi_solute - phi_matrix) / n_ws_matrix

    numerator = 2 * bulk_solute * shear_matrix * (w_solute - w_matrix) ** 2
    denominator = 3 * bulk_solute * w_matrix + 4 * shear_matrix * w_solute
    if denominator == 0:
        return 0.0
    return numerator / denominator


def _structural_solution_enthalpy(solute: str, matrix: str) -> float:
    """Return the Niessen structural enthalpy contribution for a solute-matrix direction.

    Returns:
        Structural enthalpy contribution in kJ/mol for the directional substitution.
    """
    z_solute = Element(solute).nvalence
    z_matrix = Element(matrix).nvalence

    if z_solute < _z_points[0] or z_solute > _z_points[-1]:
        return 0.0
    if not float(z_matrix).is_integer():
        return 0.0
    structure = _reference_structures.get(int(z_matrix))
    if structure is None:
        return 0.0

    def _interpolate(z: float) -> tuple[float, float]:
        index = max(0, min(bisect_right(_z_points, z) - 1, len(_z_points) - 2))
        z_0, z_1 = _z_points[index], _z_points[index + 1]
        e_0, e_1 = _niessen_energies[structure][index], _niessen_energies[structure][index + 1]
        s = (e_1 - e_0) / (z_1 - z_0)
        return e_0 + s * (z - z_0), s

    e_matrix, _ = _interpolate(z_matrix)
    e_solute, slope = _interpolate(z_solute)
    return e_matrix - e_solute + (z_solute - z_matrix) * slope


@dataclass(frozen=True)
class _MiedemaPairData:
    """Cached directional Miedema quantities for a single binary pair and composition."""

    symbol_a: str
    symbol_b: str
    c_a: float
    c_b: float
    h_ab: float
    h_ba: float
    V_A: float
    V_B: float
    pA: dict[str, float | bool | int]
    pB: dict[str, float | bool | int]
    c_a_s: float
    c_b_s: float
    f_b_a: float
    f_a_b: float

    @classmethod
    def from_pair(
        cls,
        symbol_a: str,
        symbol_b: str,
        c_a: float,
        c_b: float,
    ) -> _MiedemaPairData:
        """Build cached pair data for the given symbols and normalized fractions.

        Returns:
            Cached directional quantities for the binary pair.
        """
        pA, pB = _params[symbol_a], _params[symbol_b]
        phi_A, nws_A, V_A, tm_A = pA["phi_star"], pA["n_ws"], pA["V_molar"], pA["is_transition_metal"]
        phi_B, nws_B, V_B, tm_B = pB["phi_star"], pB["n_ws"], pB["V_molar"], pB["is_transition_metal"]

        if tm_A and tm_B:
            p_const = 1.15 * 12.35
        elif tm_A == tm_B:
            p_const = 12.35 / 1.15
        else:
            p_const = 12.35

        if pA["is_transition_metal"] == pB["is_transition_metal"]:
            r_over_p = 0.0
        else:
            factor_a = pA.get("r_over_p", 1.0 if tm_A else 0.0)
            factor_b = pB.get("r_over_p", 1.0 if tm_B else 0.0)
            r_over_p = factor_a * factor_b

        nws_A13, nws_B13 = nws_A ** (1 / 3), nws_B ** (1 / 3)
        n_denom = nws_A13 ** (-1) + nws_B13 ** (-1)
        dphi = phi_A - phi_B
        dn = nws_A13 - nws_B13
        miedema_func = -(dphi**2) + 9.4 * (dn**2) - r_over_p

        h_ab = 2 * _corrected_volume_term(symbol_a, V_A, dphi, 1.0) * p_const * miedema_func / n_denom
        h_ba = 2 * _corrected_volume_term(symbol_b, V_B, -dphi, 1.0) * p_const * miedema_func / n_denom
        h_ab = _interfacial_table.get(symbol_a, {}).get(symbol_b, h_ab)
        h_ba = _interfacial_table.get(symbol_b, {}).get(symbol_a, h_ba)

        v_a_23, v_b_23 = V_A ** (2 / 3), V_B ** (2 / 3)
        denom = c_a * v_a_23 + c_b * v_b_23
        c_a_s = c_a * v_a_23 / denom
        c_b_s = c_b * v_b_23 / denom
        f_b_a = c_b_s * (1 + 8 * (c_a_s * c_b_s) ** 2)
        f_a_b = c_a_s * (1 + 8 * (c_b_s * c_a_s) ** 2)

        return cls(
            symbol_a=symbol_a,
            symbol_b=symbol_b,
            c_a=c_a,
            c_b=c_b,
            h_ab=h_ab,
            h_ba=h_ba,
            V_A=V_A,
            V_B=V_B,
            pA=pA,
            pB=pB,
            c_a_s=c_a_s,
            c_b_s=c_b_s,
            f_b_a=f_b_a,
            f_a_b=f_a_b,
        )

    def elastic_enthalpies(self) -> tuple[float, float]:
        """Return the directional elastic mismatch enthalpies for the pair.

        Returns:
            Elastic mismatch enthalpies in kJ/mol for A in B and B in A.
        """
        h_el_ab = _elastic_solution_enthalpy(
            self.symbol_a,
            self.pA["bulk_modulus"],
            self.pB["shear_modulus"],
            self.V_A,
            self.V_B,
            self.pA["phi_star"],
            self.pB["phi_star"],
            self.pA["n_ws"],
            self.pB["n_ws"],
            self.c_b_s,
        )
        h_el_ba = _elastic_solution_enthalpy(
            self.symbol_b,
            self.pB["bulk_modulus"],
            self.pA["shear_modulus"],
            self.V_B,
            self.V_A,
            self.pB["phi_star"],
            self.pA["phi_star"],
            self.pB["n_ws"],
            self.pA["n_ws"],
            self.c_a_s,
        )
        return h_el_ab, h_el_ba

    def structural_enthalpies(self) -> tuple[float, float]:
        """Return the directional Niessen structural enthalpy contributions for the pair.

        Returns:
            Structural enthalpies in kJ/mol for A in B and B in A.
        """
        return (
            _structural_solution_enthalpy(self.symbol_a, self.symbol_b),
            _structural_solution_enthalpy(self.symbol_b, self.symbol_a),
        )


def _validate_pair(pair: tuple[str, str] | list[str]) -> tuple[str, str]:
    """Validate an element pair input and return the normalized two-symbol tuple.

    Returns:
        Validated pair of element symbols.
    """
    if not isinstance(pair, tuple | list):
        raise TypeError("Usage: MiedemaEnthalpy(('X', 'Y')) where X and Y are element names.")
    A, B = pair
    for el in (A, B):
        if el not in _params:
            raise MissingMiedemaDataError(f"No Miedema parameters for element '{el}'")
    return A, B


def _normalize_fractions(c_a: float, c_b: float) -> tuple[float, float]:
    """Normalize two composition fractions so they sum to 1.

    Returns:
        Dimensionless fractions normalized to a unit sum.
    """
    total = c_a + c_b
    if total <= 0:
        raise ValueError("Pair fractions must sum to a positive value.")
    return c_a / total, c_b / total


def _directional_ordered_enthalpies(
    solute: str,
    matrix: str,
    c_solute: float,
    c_matrix: float,
) -> tuple[float, float]:
    r"""Return the directional ordered enthalpies used to sign $\Delta G_{\text{max}}$.

    Returns:
        Ordered enthalpies in kJ/mol for solute in matrix and the reverse direction.
    """
    pair_data = _MiedemaPairData.from_pair(solute, matrix, c_solute, c_matrix)
    h_el_ab, h_el_ba = pair_data.elastic_enthalpies()
    h_struct_ab, h_struct_ba = pair_data.structural_enthalpies()

    return (
        pair_data.f_b_a * (pair_data.h_ab + h_el_ab + h_struct_ab),
        pair_data.f_a_b * (pair_data.h_ba + h_el_ba + h_struct_ba),
    )


def MiedemaIntEnthalpy(
    pair: tuple[str, str] | list[str],
    c_a: float = 0.5,
    c_b: float = 0.5,
) -> float:
    r"""Binary intermetallic interaction parameter $H_{int}$ in kJ/mol (chemical term only).

    Computes the chemical/interface term $H_{chem}$ only, without the elastic mismatch
    correction. Used for the ordered intermetallic reference energy $\Delta G_{\text{max}}$ in
    King *et al.* (2016) Eq. S.9.

    Args:
        pair (tuple or list): Element pair, e.g. ``("Fe", "Ni")``.
        c_a (float): Fraction of the first element in the binary subsystem before normalization.
        c_b (float): Fraction of the second element in the binary subsystem before normalization.

    Returns:
        $H_{int}$ in kJ/mol.

    Raises:
        TypeError: If pair is not a tuple or list.
        MissingMiedemaDataError: If Miedema parameters are unavailable for either element.

    References:
        - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179. Supplementary Eq. S.9.
    """
    A, B = _validate_pair(pair)
    c_a, c_b = _normalize_fractions(c_a, c_b)

    pair_data = _MiedemaPairData.from_pair(A, B, c_a, c_b)
    return (pair_data.c_a_s * pair_data.f_b_a * pair_data.h_ab + pair_data.c_b_s * pair_data.f_a_b * pair_data.h_ba) / 2


def MiedemaEnthalpy(
    pair: tuple[str, str] | list[str],
    c_a: float = 0.5,
    c_b: float = 0.5,
) -> float:
    r"""Binary interaction parameter $H_{ij}$ in kJ/mol from the Miedema macroscopic atom model.

    Args:
        pair (tuple or list): Element pair, e.g. ``("Fe", "Ni")``.
        c_a (float): Fraction of the first element in the binary subsystem before normalization.
        c_b (float): Fraction of the second element in the binary subsystem before normalization.

    Returns:
        $H_{ij}$ in kJ/mol.

    Raises:
        TypeError: If pair is not a tuple or list.
        MissingMiedemaDataError: If Miedema parameters are unavailable for either element.

    References:
        - de Boer, F.R.; Boom, R.; Mattens, W.C.M.; Miedema, A.R.; Niessen, A.K.
            Cohesion in Metals: Transition Metal Alloys. North-Holland, Amsterdam, 1988.
            Tables V-1.1 and V-3.
        - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B.
            Acta Mater. 2016, 104, 172-179. Supplementary Eqs. S4-S7.
        - Niessen, A.K.; Miedema, A.R.
            Ber. Bunsenges. Phys. Chem. 1983, 87, 717-723. Eq. 9 and Table I.
    """
    A, B = _validate_pair(pair)
    c_a, c_b = _normalize_fractions(c_a, c_b)

    pair_data = _MiedemaPairData.from_pair(A, B, c_a, c_b)

    h_chem = pair_data.c_a * pair_data.c_b * (pair_data.c_b_s * pair_data.h_ab + pair_data.c_a_s * pair_data.h_ba)

    h_el_ab, h_el_ba = pair_data.elastic_enthalpies()
    h_el = pair_data.c_a * pair_data.c_b * (pair_data.c_b * h_el_ab + pair_data.c_a * h_el_ba)

    h_struct_ab, h_struct_ba = pair_data.structural_enthalpies()
    h_struct = pair_data.c_a * pair_data.c_b * (pair_data.c_b * h_struct_ab + pair_data.c_a * h_struct_ba)

    return h_chem + h_el + h_struct
