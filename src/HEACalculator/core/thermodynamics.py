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
    def atomic_size_difference_cn12(self) -> float:
        """Atomic size difference computed with CN12 (Smithells/Goldschmidt) radii.

        Uses the same Fang et al. (2003) formula as atomic_size_difference but with
        CN12 corrected radii, enabling direct comparison with Senkov & Miracle (2016)
        Table 1 delta values.

        References:
            Fang, S.S.; Xiao, X.S.; Xia, L.; Li, W.H.; Dong, Y.D. J. Non-Cryst. Solids 2003, 321, 120-125.
            Senkov, O.N.; Miracle, D.B. J. Alloys Compd. 2016, 658, 603-607.
        """
        _delta = sum(
            pct * (1 - (r / self._c.average_atomic_radius_cn12)) ** 2
            for pct, r in zip(
                self._c.atomic_percentage.values(),
                self._c.atomic_radius_cn12_list,
                strict=True,
            )
        )
        return math.sqrt(_delta) * 100

    @cached_property
    def electronegativity_difference(self) -> float:
        """Allen electronegativity difference (delta_chi_Allen) of the alloy in %.

        References:
            Mann, J.B.; Meek, T.L.; Allen, L.C. J. Am. Chem. Soc. 2000, 122, 2780-2783.
            Mann, J.B.; Meek, T.L.; Knight, E.T.; Capitani, J.F.; Allen, L.C.
                J. Am. Chem. Soc. 2000, 122, 5132-5137.
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
    def min_formation_enthalpy(self) -> float:
        """Minimum binary formation enthalpy in meV/atom."""
        return min(FormationEnthalpy(pair) for pair in self._c.pair_list)

    @cached_property
    def max_formation_enthalpy(self) -> float:
        """Maximum binary formation enthalpy in meV/atom."""
        return max(FormationEnthalpy(pair) for pair in self._c.pair_list)

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

    def _compute_se_at_packing(self, xi: float) -> float:
        """S_E / k_B at a given packing fraction xi (dimensionless).

        Implements the Manssori-Carnahan-Starling-Leland (MCSL) hard-sphere mixture
        equations from the Appendix of Ye et al. (eqs. 3A-4B). Returns a dimensionless
        value that is zero for identical atom sizes and negative otherwise.

        Args:
            xi (float): Total atomic packing fraction (0.68 for BCC, 0.74 for FCC).

        References:
            Ye, Y.F. et al. Intermetallics 2015, 59, 75-80. (Appendix, eqs. 3A-4B)
            Manssori, G.A.; Carnahan, N.F.; Starling, K.E.; Leland, T.W.J.
                J. Chem. Phys. 1971, 54, 1523.
        """
        fractions = list(self._c.atomic_percentage.values())
        diameters = [2.0 * r for r in self._c.atomic_radius_list]
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
        """Excess configurational entropy S_E in J/K.mol, averaged over BCC and FCC packing.

        Always negative or zero. Zero when all atomic radii are identical.

        References:
            Ye, Y.F. et al. Intermetallics 2015, 59, 75-80. (Appendix, eqs. 3A-4B)
            Manssori, G.A.; Carnahan, N.F.; Starling, K.E.; Leland, T.W.J.
                J. Chem. Phys. 1971, 54, 1523.
        """
        se_fcc = self._compute_se_at_packing(0.74)
        se_bcc = self._compute_se_at_packing(0.68)
        return GAS_CONSTANT * (se_fcc + se_bcc) / 2

    @cached_property
    def phi(self) -> float:
        """Phi parameter: (S_C - S_H) / |S_E|.

        S_H = |H_a| / T_m is the complementary entropy derived from the mixing enthalpy.
        Large phi indicates entropic dominance and favors solid-solution formation.
        Critical threshold: phi_c ~= 20.

        References:
            Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. Scr. Mater. 2015, 104, 53-55.
            Ye, Y.F. et al. Intermetallics 2015, 59, 75-80.
        """
        if self.melting_temperature == 0:
            return math.inf
        se = self.excess_entropy
        if se == 0:
            return math.inf
        s_h = abs(self.mixing_enthalpy) * 1000 / self.melting_temperature
        return (self.mixing_entropy - s_h) / abs(se)

    @cached_property
    def delta_g_ss(self) -> float:
        """Gibbs free energy of the disordered solid solution in kJ/mol (King et al. 2016).

        References:
            King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        return self.mixing_enthalpy - self.melting_temperature * self.mixing_entropy / 1000

    @cached_property
    def delta_g_max(self) -> float:
        """delta_G_max: largest-magnitude binary compound energy in kJ/mol (King et al. 2016).

        References:
            King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
        """
        pair_enthalpies = [MixingEnthalpy(pair) for pair in self._c.pair_list]
        return len(self._c.alloy) * max(pair_enthalpies, key=abs)
