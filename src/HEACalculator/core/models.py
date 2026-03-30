"""Solid-solution formation prediction models for HEAs."""

from __future__ import annotations

import math
from functools import cached_property
from typing import TYPE_CHECKING

_J_PER_MOL_TO_MEV_PER_ATOM = _KJ_PER_MOL_TO_EV_PER_ATOM = (
    0.0103642688  # 1 J/mol = 0.010364 meV/atom | 1 kJ/mol = 0.010364 eV/atom
)
_MEV_PER_ATOM_TO_KJ_PER_MOL = 1e-3 / _KJ_PER_MOL_TO_EV_PER_ATOM

if TYPE_CHECKING:
    from HEACalculator.core.composition import AlloyComposition
    from HEACalculator.core.thermodynamics import HEAThermodynamics

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"


class SolidSolutionPredictor:
    """Applies published solid-solution formation criteria to an HEA composition.

    Each property independently computes the required thermodynamic parameters
    via the provided HEAThermodynamics instance and returns ``"Solid Solution"``,
     ``"Intermetallic"`` or ``"Multiple Phases"``.

    Args:
        composition (AlloyComposition): Parsed alloy composition.
        thermodynamics (HEAThermodynamics): Thermodynamics calculator for the same composition.
    """

    def __init__(self, composition: AlloyComposition, thermodynamics: HEAThermodynamics) -> None:
        """Initialize with parsed composition and a thermodynamics calculator."""
        self._c = composition
        self._t = thermodynamics

    @cached_property
    def microstructure(self) -> str:
        """Expected crystal structure based on VEC.

        Returns:
            One of ``"FCC"``, ``"BCC"``, ``"HCP"``, or ``"BCC+FCC"``.

        References:
            - Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
        """
        vec = self._t.valence_electron_concentration
        if 2.5 <= vec <= 3.5:
            return "HCP"
        if vec >= 8.0:
            return "FCC"
        if vec <= 6.87:
            return "BCC"
        return "BCC+FCC"

    @cached_property
    def model_1(self) -> str:
        r"""Yang & Zhang criteria: $\Omega$ >= 1.1 and $\delta$ <= 6.6.

        Returns:
            ``"Solid Solution"`` or ``"Intermetallic"``.

        References:
            - Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        """
        return "Solid Solution" if self._t.omega >= 1.1 and self._t.atomic_size_difference <= 6.6 else "Intermetallic"

    @cached_property
    def model_2(self) -> str:
        r"""Guo *et al.* criteria: -11.6 < $\Delta H_{\text{mix}}$ < 3.2 and $\delta$ < 6.6.

        Returns:
            ``"Solid Solution"`` or ``"Intermetallic"``.

        References:
            - Guo, S.; Hu, Q.; Ng, C.; Liu, C.T. Intermetallics 2013, 41, 96-103.
        """
        return (
            "Solid Solution"
            if -11.6 < self._t.mixing_enthalpy < 3.2 and self._t.atomic_size_difference < 6.6
            else "Intermetallic"
        )

    @cached_property
    def model_3(self) -> str:
        r"""Wang *et al.* criteria: $\gamma$ < 1.175.

        Returns:
            ``"Solid Solution"`` or ``"Intermetallic"``.

        References:
            - Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T. Scr. Mater. 2015, 94, 28-31.
        """
        return "Solid Solution" if self._t.gamma < 1.175 else "Intermetallic"

    @cached_property
    def model_4(self) -> str:
        r"""Singh *et al.* criteria: $\lambda$ > 0.96 (DSS), 0.24 <= $\lambda$ <= 0.96 (DSS + Compound), $\lambda$ < 0.24 (Compound).

        Returns:
            ``"Solid Solution"``, ``"Multiple Phases"``, or ``"Intermetallic"``.

        References:
            - Singh, A.K.; Kumar, N.; Dwivedi, A.; Subramaniam, A. Intermetallics 2014, 53, 112-119.
        """
        lam = self._t.lambda_
        if lam > 0.96:
            return "Solid Solution"
        if lam >= 0.24:
            return "Multiple Phases"
        return "Intermetallic"

    @cached_property
    def model_5(self) -> str:
        r"""Ye *et al.* criteria: $\phi = (S_C - S_H) / |S_E| >= 20$.

        Returns:
            ``"Solid Solution"`` or ``"Multiple Phases"``.

        References:
            - Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. Scr. Mater. 2015, 104, 53-55.
        """
        phi = self._t.phi
        if not math.isfinite(phi):
            return "Solid Solution"
        return "Solid Solution" if phi >= 20 else "Multiple Phases"

    @cached_property
    def model_6(self) -> str:
        r"""Troparevsky *et al.* criteria: all binary $\Delta H_f$ within [$-T_{crit}*\Delta S_{\text{mix}}$, 37 meV/atom].

        Returns:
            ``"Solid Solution"`` or ``"Multiple Phases"``.

        References:
            - Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. Phys. Rev. X 2015, 5(1), 011041.
        """
        critical_temperature = self._t.critical_temperature
        lower_bound = -critical_temperature * self._t.mixing_entropy * _J_PER_MOL_TO_MEV_PER_ATOM
        return (
            "Solid Solution"
            if lower_bound < self._t.min_formation_enthalpy and self._t.max_formation_enthalpy < 37.0
            else "Multiple Phases"
        )

    def model_7_k1(self) -> float:
        r"""Model 7 $k_1 = \Delta H_{\text{IM}}$ / $\Delta H_{\text{mix}}$.

        Returns:
            The dimensionless ``k1`` ratio, or ``math.inf`` when ``deltaH_mix`` is zero.
        """
        if self._t.mixing_enthalpy == 0:
            return math.inf
        return (self._t.formation_enthalpy * _MEV_PER_ATOM_TO_KJ_PER_MOL) / self._t.mixing_enthalpy

    def model_7_k1_critical(
        self,
        k_2: float = 0.6,
        annealing_temperature: float | None = None,
    ) -> float:
        r"""Model 7 critical $k_1$ threshold at the given annealing temperature.

        Returns:
            Dimensionless critical ``k1`` threshold for the supplied annealing condition.
        """
        if annealing_temperature is None:
            annealing_temperature = self._t.critical_temperature
        omega = self._t.omega_at(annealing_temperature)
        return omega * (1 - k_2) + 1

    def model_7(
        self,
        k_2: float = 0.6,
        annealing_temperature: float | None = None,
    ) -> str:
        r"""Senkov & Miracle criteria.

        Args:
            k_2 (float): Ratio of intermetallic and mixing entropies. Defaults to 0.6.
            annealing_temperature (float, optional): Temperature in Kelvin for the Omega calculation.
                Defaults to 55% of $T_m$.

        Returns:
            ``"Solid Solution"`` or ``"Intermetallic"``.

        References:
            - Senkov, O.N.; Miracle, D.B. J. Alloys Compd. 2016, 658, 603-607.
        """
        if annealing_temperature is None:
            annealing_temperature = self._t.critical_temperature
        if self._t.mixing_enthalpy == 0:
            return "Intermetallic"
        return (
            "Solid Solution"
            if self.model_7_k1_critical(k_2=k_2, annealing_temperature=annealing_temperature) > self.model_7_k1()
            else "Intermetallic"
        )

    @cached_property
    def model_8(self) -> str:
        r"""King *et al.* criteria: $\phi = $\Delta G_{\text{SS}}$ / (−|$\Delta G_{\text{max}}$|) >= 1$.

        Returns:
            ``"Solid Solution"`` or ``"Multiple Phases"``.

        References:
            - King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        return "Solid Solution" if self._t.f_parameter >= 1 else "Multiple Phases"
