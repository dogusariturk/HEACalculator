"""Thermodynamic and structural property calculations for HEAs."""

from __future__ import annotations

import math
from functools import cached_property
from typing import TYPE_CHECKING, Literal

import numpy as np

if TYPE_CHECKING:
    from HEACalculator.core.composition import AlloyComposition
from HEACalculator.data.formation_enthalpy import FormationEnthalpy
from HEACalculator.data.mixing_enthalpy import MixingEnthalpy

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

    @cached_property
    def mixing_enthalpy(self) -> float:
        """Enthalpy of mixing of the alloy in kJ/mol.

        References:
            Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. Prog. Mater. Sci. 2014, 61, 1-93.
        """
        pair_mixing_enthalpy = [MixingEnthalpy(pair) for pair in self._c.pair_list]
        return 4 * sum(pct * h for pct, h in zip(self._c.pair_percentage, pair_mixing_enthalpy, strict=True))

    @cached_property
    def formation_enthalpy(self) -> float:
        """Formation enthalpy of the alloy in meV/atom.

        References:
            Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. Phys. Rev. X 2015, 5(1), 011041.
        """
        pair_formation_enthalpy = [FormationEnthalpy(pair) for pair in self._c.pair_list]
        return 4 * sum(pct * h for pct, h in zip(self._c.pair_percentage, pair_formation_enthalpy, strict=True))

    @cached_property
    def density(self) -> float:
        """Approximate density of the alloy in g/cm^3."""
        total_weight = sum(self._c.elements[elm].atomic_weight * af for elm, af in self._c.alloy.items())
        total_volume = sum(self._c.elements[elm].atomic_volume * af for elm, af in self._c.alloy.items())
        return total_weight / total_volume

    @cached_property
    def valence_electron_concentration(self) -> float:
        """Valence electron concentration (VEC) of the alloy.

        References:
            Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
        """
        nvalence_list = [self._c.elements[elm].nvalence for elm in self._c.alloy]
        return sum(pct * v for pct, v in zip(self._c.atomic_percentage.values(), nvalence_list, strict=True))

    @cached_property
    def melting_temperature(self) -> int | float | Literal[0]:
        """Approximate melting temperature of the alloy in Kelvin."""
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
        """Atomic size difference (delta) of the alloy.

        References:
            Fang, S.S.; Xiao, X.S.; Xia, L.; Li, W.H.; Dong, Y.D. J. Non-Cryst. Solids 2003, 321, 120-125.
        """
        _delta = sum(
            pct * (1 - (r / self._c.average_atomic_radius)) ** 2
            for pct, r in zip(
                self._c.atomic_percentage.values(),
                self._c.atomic_radius_list,
                strict=True,
            )
        )
        return math.sqrt(_delta) * 100

    @cached_property
    def min_formation_enthalpy(self) -> float:
        """Minimum binary formation enthalpy in meV/atom."""
        return min(FormationEnthalpy(pair) for pair in self._c.pair_list)

    @cached_property
    def mixing_entropy(self) -> float:
        """Configurational mixing entropy of the alloy in J/K.mol."""
        pct_array = np.array([v for v in self._c.atomic_percentage.values() if v > 0])
        return -1 * GAS_CONSTANT * sum(pct_array * np.log(pct_array))

    @cached_property
    def gamma(self) -> float:
        """Gamma parameter (solid-angle ratio of smallest/largest atoms).

        References:
            Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T. Scr. Mater. 2015, 94, 28-31.
        """
        r_min = min(self._c.atomic_radius_list)
        r_max = max(self._c.atomic_radius_list)
        r_avg = self._c.average_atomic_radius

        smallest_solid_angle = 1 - np.sqrt(((r_min + r_avg) ** 2 - r_avg**2) / (r_min + r_avg) ** 2)
        largest_solid_angle = 1 - np.sqrt(((r_max + r_avg) ** 2 - r_avg**2) / (r_max + r_avg) ** 2)
        return smallest_solid_angle / largest_solid_angle

    @cached_property
    def omega(self) -> float:
        """Omega stability parameter evaluated at the alloy's melting temperature.

        References:
            Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        """
        return self.omega_at(self.melting_temperature)

    def omega_at(self, temperature: float) -> float:
        """Omega stability parameter evaluated at *temperature*.

        Args:
            temperature (float): Temperature in Kelvin.

        References:
            Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        """
        if self.mixing_enthalpy == 0:
            return math.inf
        return (temperature * self.mixing_entropy) / (abs(self.mixing_enthalpy) * 1000)

    @cached_property
    def lambda_(self) -> float:
        """Lambda parameter (entropy / atomic-size-difference ratio).

        References:
            Singh, A.K.; Kumar, N.; Dwivedi, A.; Subramaniam, A. Intermetallics 2014, 53, 112-119.
        """
        if self.atomic_size_difference == 0:
            return math.inf
        return self.mixing_entropy / (self.atomic_size_difference**2)

    @cached_property
    def phi(self) -> float:
        """Phi parameter: Omega − 1 (Ye et al. 2015).

        References:
            Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. Scr. Mater. 2015, 104, 53-55.
        """
        if not math.isfinite(self.omega):
            return math.inf
        return self.omega - 1

    @cached_property
    def delta_g_ss(self) -> float:
        """Gibbs free energy of the disordered solid solution in kJ/mol (King et al. 2016).

        References:
            King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        return self.mixing_enthalpy - self.melting_temperature * self.mixing_entropy / 1000

    @cached_property
    def delta_g_max(self) -> float:
        """ΔG_max: largest-magnitude binary compound energy in kJ/mol (King et al. 2016).

        References:
            King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        pair_enthalpies = [MixingEnthalpy(pair) for pair in self._c.pair_list]
        return 2 * max(pair_enthalpies, key=abs)
