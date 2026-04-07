"""Thermodynamic and structural property calculations for HEAs."""

from __future__ import annotations

import math
from functools import cached_property
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from HEACalculator.core.composition import AlloyComposition
from HEACalculator.data.formation_enthalpy import FormationEnthalpy
from HEACalculator.data.miedema_enthalpy import (
    MiedemaEnthalpy,
    MiedemaIntEnthalpy,
    _directional_ordered_enthalpies,
)
from HEACalculator.data.mixing_enthalpy import MixingEnthalpy
from HEACalculator.data.model_radii import model_atomic_radius_cn12
from HEACalculator.exceptions import MissingFormationEnthalpyError, MissingMiedemaDataError, MissingMixingEnthalpyError

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

GAS_CONSTANT = 8.314462618


class HEAThermodynamics:
    """Calculates thermodynamic and structural parameters for an HEA.

    All properties are computed lazily on first access and cached.

    Args:
        composition (AlloyComposition): Parsed alloy composition to calculate properties for.
    """

    def __init__(self, composition: AlloyComposition) -> None:
        """Initialize with a parsed alloy composition."""
        self._c = composition

    def _model_atomic_radius_list(self) -> list[float]:
        """Return the per-element atomic radii used by the delta and gamma calculations.

        Returns:
            Atomic radii in pm aligned with the alloy element order.
        """
        return [self._c.elements[elm].atomic_radius for elm in self._c.alloy]

    def _model_atomic_radius_cn12_list(self) -> list[float]:
        """Return the per-element CN12 radii used by the model-specific size calculations.

        Returns:
            CN12 radii in pm aligned with the alloy element order.
        """
        return [model_atomic_radius_cn12(elm, self._c.elements[elm].atomic_radius_cn12) for elm in self._c.alloy]

    def _average_radius(self, radii: list[float]) -> float:
        """Return the composition-weighted average radius for the supplied radius list.

        Returns:
            Composition-weighted average in the same units as the input list.
        """
        return sum(pct * r for pct, r in zip(self._c.atomic_percentage.values(), radii, strict=True))

    @cached_property
    def mixing_enthalpy(self) -> float:
        """Enthalpy of mixing of the alloy in kJ/mol.

        Returns:
            Configurational mixing enthalpy in kJ/mol.

        References:
            - Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. Prog. Mater. Sci. 2014, 61, 1-93.
        """
        try:
            pair_mixing_enthalpy = [MixingEnthalpy(pair) for pair in self._c.pair_list]
        except MissingMixingEnthalpyError:
            return float("nan")
        return 4 * sum(pct * h for pct, h in zip(self._c.pair_percentage, pair_mixing_enthalpy, strict=True))

    @cached_property
    def mixing_enthalpy_miedema(self) -> float:
        """Model 8 solid-solution formation enthalpy in kJ/mol from the Miedema model.

        Returns:
            Miedema-model solid-solution enthalpy in kJ/mol.

        References:
            - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179. Supplementary Eqs. S1-S8.
            - de Boer, F.R.; Boom, R.; Mattens, W.C.M.; Miedema, A.R.; Niessen, A.K. Cohesion in Metals: Transition Metal Alloys. North-Holland, Amsterdam, 1988.
        """
        total = 0.0
        try:
            for element_i, x_i in self._c.atomic_percentage.items():
                if x_i >= 1.0:
                    continue
                remaining_fraction = 1.0 - x_i
                for element_k, x_k in self._c.atomic_percentage.items():
                    if element_k == element_i or x_k == 0.0:
                        continue
                    x_k_f = x_k / remaining_fraction
                    total += x_i * x_k_f * MiedemaEnthalpy((element_i, element_k), x_i, x_k_f)
        except MissingMiedemaDataError:
            return float("nan")
        return total

    @cached_property
    def formation_enthalpy(self) -> float:
        """Formation enthalpy of the alloy in meV/atom.

        Returns:
            Configurational formation enthalpy in meV/atom.

        References:
            - Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. Phys. Rev. X 2015, 5(1), 011041.
        """
        try:
            pair_formation_enthalpy = [FormationEnthalpy(pair) for pair in self._c.pair_list]
        except MissingFormationEnthalpyError:
            return float("nan")
        return 4 * sum(pct * h for pct, h in zip(self._c.pair_percentage, pair_formation_enthalpy, strict=True))

    @cached_property
    def density(self) -> float:
        """Approximate density of the alloy in g/cm$^3$.

        Returns:
            Estimated alloy density in g/cm$^3$.
        """
        total_weight = sum(self._c.elements[elm].atomic_weight * af for elm, af in self._c.alloy.items())
        total_volume = sum(self._c.elements[elm].atomic_volume * af for elm, af in self._c.alloy.items())
        return total_weight / total_volume

    @cached_property
    def valence_electron_concentration(self) -> float:
        """Valence electron concentration (VEC) of the alloy.

        Returns:
            Dimensionless composition-weighted valence electron concentration.

        References:
            - Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
        """
        nvalence_list = [self._c.elements[elm].nvalence for elm in self._c.alloy]
        return sum(pct * v for pct, v in zip(self._c.atomic_percentage.values(), nvalence_list, strict=True))

    @cached_property
    def melting_temperature(self) -> int | float:
        """Approximate melting temperature of the alloy in Kelvin.

        Returns:
            Estimated melting temperature rounded up when finite.
        """
        melting_temperature_list = [self._c.elements[elm].melting_point for elm in self._c.alloy]
        result = sum(
            pct * t
            for pct, t in zip(
                self._c.atomic_percentage.values(),
                melting_temperature_list,
                strict=True,
            )
        )
        return math.ceil(result) if math.isfinite(result) else result

    @cached_property
    def atomic_size_difference(self) -> float:
        r"""Atomic size difference ($\delta$) of the alloy.

        Returns:
            Atomic size difference in percent using model radii.

        References:
            - Fang, S.S.; Xiao, X.S.; Xia, L.; Li, W.H.; Dong, Y.D. J. Non-Cryst. Solids 2003, 321, 120-125.
        """
        radii = self._model_atomic_radius_list()
        average_radius = self._average_radius(radii)
        _delta = sum(
            pct * (1 - (r / average_radius)) ** 2 for pct, r in zip(self._c.atomic_percentage.values(), radii, strict=True)
        )
        return math.sqrt(_delta) * 100

    @cached_property
    def atomic_size_difference_cn12(self) -> float:
        """Atomic size difference computed with CN12 (Smithells/Goldschmidt) radii.

        Returns:
            Atomic size difference in percent using CN12 radii.

        References:
            - Fang, S.S.; Xiao, X.S.; Xia, L.; Li, W.H.; Dong, Y.D. J. Non-Cryst. Solids 2003, 321, 120-125.
            - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        radii = self._model_atomic_radius_cn12_list()
        average_radius = self._average_radius(radii)
        _delta = sum(
            pct * (1 - (r / average_radius)) ** 2 for pct, r in zip(self._c.atomic_percentage.values(), radii, strict=True)
        )
        return math.sqrt(_delta) * 100

    @cached_property
    def allen_electronegativity_difference(self) -> float:
        r"""Allen electronegativity difference (delta_chi_Allen) of the alloy in %.

        Returns:
            Allen electronegativity mismatch in percent.

        References:
            - Mann, J.B.; Meek, T.L.; Allen, L.C. J. Am. Chem. Soc. 2000, 122, 2780-2783.
            - Mann, J.B.; Meek, T.L.; Knight, E.T.; Capitani, J.F.; Allen, L.C. J. Am. Chem. Soc. 2000, 122, 5132-5137.
        """
        chi_avg = self._c.average_allen_electronegativity
        _delta_chi = sum(
            pct * (1 - (x / chi_avg)) ** 2
            for pct, x in zip(
                self._c.atomic_percentage.values(),
                self._c.allen_electronegativity_list,
                strict=True,
            )
        )
        return math.sqrt(_delta_chi) * 100

    @cached_property
    def pauling_electronegativity_difference(self) -> float:
        r"""Pauling electronegativity difference (delta_chi_Pauling) of the alloy in %.

        Returns:
            Pauling electronegativity mismatch in percent.

        References:
            - Haynes, W.M. CRC Handbook of Chemistry and Physics, 95th ed.;
              CRC Press: London, 2014. ISBN 9781482208689.
        """
        chi_avg = self._c.average_pauling_electronegativity
        _delta_chi = sum(
            pct * (1 - (x / chi_avg)) ** 2
            for pct, x in zip(
                self._c.atomic_percentage.values(),
                self._c.pauling_electronegativity_list,
                strict=True,
            )
        )
        return math.sqrt(_delta_chi) * 100

    @cached_property
    def min_formation_enthalpy(self) -> float:
        """Minimum binary formation enthalpy in meV/atom.

        Returns:
            Lowest binary formation enthalpy among all alloy pairs.
        """
        if not self._c.pair_list:
            return 0.0
        try:
            return min(FormationEnthalpy(pair) for pair in self._c.pair_list)
        except MissingFormationEnthalpyError:
            return float("nan")

    @cached_property
    def max_formation_enthalpy(self) -> float:
        """Maximum binary formation enthalpy in meV/atom.

        Returns:
            Highest binary formation enthalpy among all alloy pairs.
        """
        if not self._c.pair_list:
            return 0.0
        try:
            return max(FormationEnthalpy(pair) for pair in self._c.pair_list)
        except MissingFormationEnthalpyError:
            return float("nan")

    @cached_property
    def mixing_entropy(self) -> float:
        """Configurational mixing entropy of the alloy in J/K.mol.

        Returns:
            Configurational mixing entropy in J/K.mol.
        """
        pct_array = np.array([v for v in self._c.atomic_percentage.values() if v > 0])
        return -1 * GAS_CONSTANT * sum(pct_array * np.log(pct_array))

    @cached_property
    def gamma(self) -> float:
        """Gamma parameter (solid-angle ratio of smallest/largest atoms).

        Returns:
            Dimensionless gamma parameter from the alloy radius distribution.

        References:
            - Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T. Scr. Mater. 2015, 94, 28-31.
        """
        radii = self._model_atomic_radius_list()
        r_min, r_max = min(radii), max(radii)
        r_avg = self._average_radius(radii)

        smallest_solid_angle = 1 - np.sqrt(((r_min + r_avg) ** 2 - r_avg**2) / (r_min + r_avg) ** 2)
        largest_solid_angle = 1 - np.sqrt(((r_max + r_avg) ** 2 - r_avg**2) / (r_max + r_avg) ** 2)
        return smallest_solid_angle / largest_solid_angle

    @cached_property
    def omega(self) -> float:
        """Omega stability parameter evaluated at the alloy's melting temperature.

        Returns:
            Dimensionless omega stability parameter at ``melting_temperature``.

        References:
            - Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        """
        return self.omega_at(self.melting_temperature)

    def omega_at(self, temperature: float) -> float:
        """Omega stability parameter evaluated at *temperature*.

        Args:
            temperature (float): Temperature in Kelvin.

        Returns:
            Dimensionless omega stability parameter at the supplied temperature.

        References:
            - Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        """
        if self.mixing_enthalpy == 0:
            return math.inf
        return (temperature * self.mixing_entropy) / (abs(self.mixing_enthalpy) * 1000)

    @cached_property
    def lambda_(self) -> float:
        """Lambda parameter (entropy / atomic-size-difference ratio).

        Uses CN12 (Goldschmidt/Smithells) radii for delta.

        Returns:
            Dimensionless lambda parameter, or ``math.inf`` when the CN12 delta is zero.

        References:
            - Singh, A.K.; Kumar, N.; Dwivedi, A.; Subramaniam, A. Intermetallics 2014, 53, 112-119.
        """
        if self.atomic_size_difference_cn12 == 0:
            return math.inf
        return self.mixing_entropy / (self.atomic_size_difference_cn12**2)

    def _compute_se_at_packing(self, xi: float) -> float:
        """S_E / k_B at a given packing fraction xi (dimensionless).

        Implements the Manssori-Carnahan-Starling-Leland (MCSL) hard-sphere mixture
        equations from the Appendix of Ye *et al.* (eqs. 3A-4B). Returns a dimensionless
        value that is zero for identical atom sizes and negative otherwise.

        Args:
            xi (float): Total atomic packing fraction (0.68 for BCC, 0.74 for FCC).

        Returns:
            Dimensionless excess entropy contribution at the given packing fraction.

        References:
            - Ye, Y.F. et al. Intermetallics 2015, 59, 75-80.
            - Manssori, G.A.; Carnahan, N.F.; Starling, K.E.; Leland, T.W.J. J. Chem. Phys. 1971, 54, 1523.
        """
        fractions = list(self._c.atomic_percentage.values())
        diameters = [2.0 * r for r in self._model_atomic_radius_cn12_list()]
        n = len(fractions)

        d3 = [d**3 for d in diameters]
        denom = sum(c * d3i for c, d3i in zip(fractions, d3, strict=True))
        xi_i = [xi * c * d3i / denom for c, d3i in zip(fractions, d3, strict=True)]

        k_sum = sum((xi_i[k] / xi) / diameters[k] for k in range(n))

        y1 = y2 = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                di, dj = diameters[i], diameters[j]
                ci, cj = fractions[i], fractions[j]
                sqrt_didj = math.sqrt(di * dj)
                size_term = (di - dj) ** 2 / (di * dj)
                d_val = (math.sqrt(xi_i[i] * xi_i[j]) / xi) * size_term * math.sqrt(ci * cj)
                y1 += d_val * (di + dj) / sqrt_didj
                y2 += d_val * sqrt_didj * k_sum
        y3 = sum((xi_i[i] / xi) ** (2.0 / 3.0) * fractions[i] ** (1.0 / 3.0) for i in range(n)) ** 3

        z = (1 + xi + xi**2 - 3 * xi * (y1 + y2 * xi) - xi**3 * y3) / (1 - xi) ** 3

        f_ex = (
            -1.5 * (1 - y1 + y2 + y3)
            + (3 * y2 + 2 * y3) / (1 - xi)
            + 1.5 * (1 - y1 - y2 - y3 / 3.0) / (1 - xi) ** 2
            + (y3 - 1) * math.log(1 - xi)
        )

        return f_ex - math.log(z) - (3 - 2 * xi) / (1 - xi) ** 2 + 3 + math.log((1 + xi + xi**2 - xi**3) / (1 - xi) ** 3)

    @cached_property
    def excess_entropy(self) -> float:
        """Excess configurational entropy $S_E$ in J/K.mol, averaged over BCC and FCC packing.

        Always negative or zero. Zero when all atomic radii are identical.

        Returns:
            Excess configurational entropy in J/K.mol.

        References:
            - Ye, Y.F. et al. Intermetallics 2015, 59, 75-80. (Appendix, eqs. 3A-4B)
            - Manssori, G.A.; Carnahan, N.F.; Starling, K.E.; Leland, T.W.J. J. Chem. Phys. 1971, 54, 1523.
        """
        return GAS_CONSTANT * (self._compute_se_at_packing(0.74) + self._compute_se_at_packing(0.68)) / 2

    @cached_property
    def phi_fcc(self) -> float:
        r"""Model 5 phi parameter using the FCC packing fraction reported in the supplement.

        Returns:
            Dimensionless phi value evaluated at FCC packing.
        """
        return self._phi_at_packing(0.74)

    @cached_property
    def phi_bcc(self) -> float:
        r"""Model 5 phi parameter using the BCC packing fraction reported in the supplement.

        Returns:
            Dimensionless phi value evaluated at BCC packing.
        """
        return self._phi_at_packing(0.68)

    def _phi_at_packing(self, xi: float) -> float:
        r"""Return the Model 5 phi value at the given packing fraction.

        Returns:
            Dimensionless phi value for the supplied packing fraction.
        """
        if self.melting_temperature == 0:
            return math.inf
        se = GAS_CONSTANT * self._compute_se_at_packing(xi)
        if se == 0:
            return math.inf
        s_h = abs(self.mixing_enthalpy) * 1000 / self.melting_temperature
        return (self.mixing_entropy - s_h) / abs(se)

    @cached_property
    def phi(self) -> float:
        r"""$\phi$ parameter: $(S_C - S_H) / |S_E|$.

        $S_H = |H_a| / T_m$ is the complementary entropy derived from the mixing enthalpy.
        H_a uses the Takeuchi & Inoue (2000) binary mixing enthalpy table (Miedema model,
        Bakker 1998 parameterization), as cited by Ye *et al.* (2015) refs [5,14].
        $S_E$ uses the MCSL hard-sphere model with CN12 (Goldschmidt) radii.

        Returns:
            Dimensionless average of the FCC and BCC phi values, or ``math.inf`` when either diverges.

        References:
            - Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. Scr. Mater. 2015, 104, 53-55.
            - Ye, Y.F. et al. Intermetallics 2015, 59, 75-80.
            - Takeuchi, A.; Inoue, A. Mater. Trans. JIM 2000, 41, 1372-1378.
        """
        phi_fcc = self.phi_fcc
        phi_bcc = self.phi_bcc
        if math.isnan(phi_fcc) or math.isnan(phi_bcc):
            return float("nan")
        if not math.isfinite(phi_fcc) or not math.isfinite(phi_bcc):
            return math.inf
        return (phi_fcc + phi_bcc) / 2

    @cached_property
    def critical_temperature(self) -> float:
        r"""Critical temperature $T_crit = 0.55 * T_m$, used by Models 6 and 7.

        Returns:
            55% of the composition-weighted melting temperature in Kelvin.
        """
        return self.melting_temperature * 0.55

    @cached_property
    def delta_g_ss(self) -> float:
        """Gibbs free energy of the disordered solid solution in kJ/mol.

        Returns:
            Disordered solid-solution Gibbs free energy in kJ/mol.

        References:
            - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        return self.mixing_enthalpy_miedema - self.melting_temperature * self.mixing_entropy / 1000

    @cached_property
    def delta_g_max(self) -> float:
        r"""$\Delta G_{\text{max}}$: largest-magnitude binary intermetallic energy scaled to alloy stoichiometry, in kJ/mol.

        The binary intermetallic enthalpy is computed from the Miedema model (Eq. S9).
        The largest-magnitude binary value is scaled by j/2 (half the number of elements)
        to account for the maximum number of binary intermetallic pairs that can form from
        j elements while maintaining stoichiometry.

        Returns:
            Largest-magnitude ordered intermetallic energy contribution in kJ/mol.

        References:
            - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        pair_enthalpies: list[float] = []
        try:
            for pair in self._c.pair_list:
                ca, cb = self._c.atomic_percentage[pair[0]], self._c.atomic_percentage[pair[1]]
                total = ca + cb
                if total <= 0:
                    continue
                c_a, c_b = ca / total, cb / total
                h_dir_ab, h_dir_ba = _directional_ordered_enthalpies(pair[0], pair[1], c_a, c_b)
                miedema_pair = MiedemaIntEnthalpy(pair, ca, cb)
                direction_sign = h_dir_ab if abs(h_dir_ab) >= abs(h_dir_ba) else h_dir_ba
                if direction_sign == 0:
                    pair_enthalpies.append(miedema_pair)
                else:
                    pair_enthalpies.append(math.copysign(abs(miedema_pair), direction_sign))
        except MissingMiedemaDataError:
            return float("nan")
        if not pair_enthalpies:
            return 0.0
        pos_max = max(pair_enthalpies)
        neg_min = min(pair_enthalpies)
        largest = pos_max if pos_max >= -neg_min else neg_min
        return (len(self._c.alloy) // 2) * largest

    @cached_property
    def f_parameter(self) -> float:
        r"""Model 8 F parameter: $\Delta G_{\text{SS}} / (-|\Delta G_{\text{max}}|)$.

        Returns:
            Dimensionless model 8 ``F`` parameter, or ``math.inf`` when ``\Delta G_{\text{max}}`` is zero.
        """
        if self.delta_g_max == 0:
            return math.inf
        return self.delta_g_ss / (-abs(self.delta_g_max))
