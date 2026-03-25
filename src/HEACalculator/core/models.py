"""Solid-solution formation prediction models for HEAs."""

from __future__ import annotations

import math
from functools import cached_property
from typing import TYPE_CHECKING

_KJ_PER_MOL_TO_EV_PER_ATOM = 0.0103642688  # 1 kJ/mol = 0.010364 eV/atom
_J_PER_MOL_TO_EV_PER_ATOM = _KJ_PER_MOL_TO_EV_PER_ATOM / 1000
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
            str: One of ``"FCC"``, ``"BCC"``, ``"HCP"``, or ``"BCC+FCC"``.

        References:
            Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
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
        """Yang & Zhang criteria: Omega >= 1.1 and delta <= 6.6.

        References:
            Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        """
        return "Solid Solution" if self._t.omega >= 1.1 and self._t.atomic_size_difference <= 6.6 else "Intermetallic"

    @cached_property
    def model_2(self) -> str:
        """Guo et al. criteria: -11.6 < deltaH_mix < 3.2 and delta < 6.6.

        References:
            Guo, S.; Hu, Q.; Ng, C.; Liu, C.T. Intermetallics 2013, 41, 96-103.
        """
        return (
            "Solid Solution"
            if -11.6 < self._t.mixing_enthalpy < 3.2 and self._t.atomic_size_difference < 6.6
            else "Intermetallic"
        )

    @cached_property
    def model_3(self) -> str:
        """Wang et al. criteria: Omega >= 1.1 and Gamma < 1.175.

        References:
            Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T. Scr. Mater. 2015, 94, 28-31.
        """
        return "Solid Solution" if self._t.omega >= 1.1 and self._t.gamma < 1.175 else "Intermetallic"

    @cached_property
    def model_4(self) -> str:
        """Singh et al. criteria: Lambda > 0.96 (DSS), 0.24 <= Lambda <= 0.96 (DSS + Compound), Lambda < 0.24 (Compound).

        References:
            Singh, A.K.; Kumar, N.; Dwivedi, A.; Subramaniam, A. Intermetallics 2014, 53, 112-119.
        """
        lam = self._t.lambda_
        if lam > 0.96:
            return "Solid Solution"
        if lam >= 0.24:
            return "Multiple Phases"
        return "Intermetallic"

    @cached_property
    def model_5(self) -> str:
        """Ye et al. criteria: Phi = Omega - 1 >= 20.

        References:
            Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. Scr. Mater. 2015, 104, 53-55.
        """
        omega = self._t.omega
        if not math.isfinite(omega):
            return "Solid Solution"
        return "Solid Solution" if omega - 1 >= 20 else "Multiple Phases"

    @cached_property
    def model_6(self) -> str:
        """Troparevsky et al. criteria: formation enthalpy window at 0.55 T_m.

        References:
            Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. Phys. Rev. X 2015, 5(1), 011041.
        """
        critical_temperature = self._t.melting_temperature * 0.55
        return (
            "Solid Solution"
            if (-1 * 1000 * critical_temperature * self._t.mixing_entropy * _J_PER_MOL_TO_EV_PER_ATOM)
            < float(self._t.min_formation_enthalpy)
            < 37
            else "Multiple Phases"
        )

    def model_7(
        self,
        k_2: float = 0.6,
        annealing_temperature: float | None = None,
    ) -> str:
        """Senkov & Miracle criteria.

        Args:
            k_2 (float): Ratio of intermetallic and mixing entropies. Defaults to 0.6.
            annealing_temperature (float, optional): Temperature for the Omega calculation.
                Defaults to 60% of T_m.

        References:
            Senkov, O.N.; Miracle, D.B. J. Alloys Compd. 2016, 658, 603-607.
        """
        if self._t.mixing_enthalpy == 0:
            return "Intermetallic"
        if annealing_temperature is None:
            annealing_temperature = self._t.melting_temperature * 0.6
        k_1 = (self._t.formation_enthalpy * _MEV_PER_ATOM_TO_KJ_PER_MOL) / self._t.mixing_enthalpy
        omega = self._t.omega_at(annealing_temperature)
        k_1_cr = omega * (1 - k_2) + 1
        return "Solid Solution" if k_1_cr > k_1 else "Intermetallic"

    @cached_property
    def model_8(self) -> str:
        """King et al. criteria: Phi = deltaG_ss / (−|deltaG_max|) >= 1.

        References:
            King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        if self._t.delta_g_max == 0:
            return "Solid Solution"
        phi = self._t.delta_g_ss / (-abs(self._t.delta_g_max))
        return "Solid Solution" if phi >= 1 else "Multiple Phases"
