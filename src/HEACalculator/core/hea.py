"""Facade class for High Entropy Alloy calculations."""

from __future__ import annotations

import math

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.models import SolidSolutionPredictor
from HEACalculator.core.thermodynamics import HEAThermodynamics

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"
__version__ = "2.0.0"


RESULT_HEADERS = (
    "Formula",
    "Density (g/cm^3)",
    "Delta (%)",
    "Delta (CN12) (%)",
    "Delta Chi (Allen) (%)",
    "Delta Chi (Pauling) (%)",
    "Omega",
    "Gamma",
    "Lambda",
    "VEC",
    "e/a",
    "Mixing Enthalpy (kJ/mol)",
    "Mixing Entropy (J/K.mol)",
    "Formation Enthalpy (meV/atom)",
    "Min. Formation Enthalpy (meV/atom)",
    "Melting Temperature (K)",
    "Crystal Structure",
    "Model 1",
    "Model 2",
    "Model 3",
    "Model 4",
    "Model 5",
    "Model 6",
    "Model 7",
    "Model 8",
)


class HEACalculator:
    """General class for high entropy alloy calculations.

    Composes ``AlloyComposition``, ``HEAThermodynamics``, and ``SolidSolutionPredictor``
    to provide a single entry point for HEA calculations. All properties are
    computed lazily on first access via the ``thermo`` and ``predictor`` sub-objects.

    Args:
        formula (str): Alloy formula.

    Attributes:
        formula (str): The original formula string.
        thermo (HEAThermodynamics): Thermodynamic properties of the alloy.
        predictor (SolidSolutionPredictor): Solid-solution formation predictions.

    References:
        1. Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. Prog. Mater. Sci. 2014, 61, 1-93.
        2. Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. Phys. Rev. X 2015, 5(1), 011041.
        3. Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
        4. Fang, S.S.; Xiao, X.S.; Xia, L.; Li, W.H.; Dong, Y.D. J. Non-Cryst. Solids 2003, 321, 120-125.
        5. Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233-238.
        6. Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T. Scr. Mater. 2015, 94, 28-31.
        7. Singh, A.K.; Kumar, N.; Dwivedi, A.; Subramaniam, A. Intermetallics 2014, 53, 112-119.
        8. Guo, S.; Hu, Q.; Ng, C.; Liu, C.T. Intermetallics 2013, 41, 96-103.
        9. Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. Scr. Mater. 2015, 104, 53-55.
        10. Senkov, O.N.; Miracle, D.B. J. Alloys Compd. 2016, 658, 603-607.
        11. King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. Acta Mater. 2016, 104, 172-179.
    """

    @staticmethod
    def _fmt(value: float | int, spec: str = ">10.2f") -> str:
        """Format *value* with *spec*, returning 'N/A' for NaN.

        When *spec* carries an alignment character and explicit width (e.g. ``">10.2f"``),
        'N/A' is padded to that width.  Bare precision specs like ``".2f"`` return the
        unpadded string ``"N/A"``.
        """
        if isinstance(value, float) and math.isnan(value):
            align = spec[0] if spec and spec[0] in "><^=" else None
            rest = spec[1:] if align else spec
            width = rest.split(".")[0] if rest else ""
            if align and width.isdigit():
                return format("N/A", f"{align}{width}")
            return "N/A"
        return format(value, spec)

    def __init__(self, formula: str) -> None:
        """Initialize with *formula*. All properties are computed lazily via ``thermo`` and ``predictor``."""
        self.formula = formula
        composition = AlloyComposition(formula)
        self.thermo = HEAThermodynamics(composition)
        self.predictor = SolidSolutionPredictor(composition, self.thermo)

    @classmethod
    def get_headers(cls) -> list[str]:
        """Return the tabular result headers in the same order as ``get_list()``."""
        return list(RESULT_HEADERS)

    def get_dict(self) -> dict:
        """Return all calculated properties as a dict with raw numeric values.

        NaN values are returned as None for JSON compatibility.

        Returns:
            Mapping of property names to raw numeric or string values.
        """

        def _n(v: float) -> float | None:
            return None if isinstance(v, float) and math.isnan(v) else v

        t = self.thermo
        p = self.predictor
        return {
            "formula": self.formula,
            "density": _n(t.density),
            "delta": _n(t.atomic_size_difference),
            "delta_cn12": _n(t.atomic_size_difference_cn12),
            "delta_chi_allen": _n(t.allen_electronegativity_difference),
            "delta_chi_pauling": _n(t.pauling_electronegativity_difference),
            "omega": _n(t.omega),
            "gamma": _n(t.gamma),
            "lambda": _n(t.lambda_),
            "vec": _n(t.valence_electron_concentration),
            "ea_ratio": _n(t.ea_ratio),
            "mixing_enthalpy": _n(t.mixing_enthalpy),
            "mixing_entropy": _n(t.mixing_entropy),
            "formation_enthalpy": _n(t.formation_enthalpy),
            "min_formation_enthalpy": _n(t.min_formation_enthalpy),
            "melting_temperature": _n(t.melting_temperature),
            "microstructure": p.microstructure,
            "model_1": p.model_1,
            "model_2": p.model_2,
            "model_3": p.model_3,
            "model_4": p.model_4,
            "model_5": p.model_5,
            "model_6": p.model_6,
            "model_7": p.model_7(),
            "model_8": p.model_8,
        }

    def get_list(self) -> list:
        """Return all calculated properties as a formatted list.

        Returns:
            Formula, thermodynamic values, and model predictions formatted for tabular output.
        """
        t = self.thermo
        p = self.predictor
        result = [self.formula]
        for item in [
            t.density,
            t.atomic_size_difference,
            t.atomic_size_difference_cn12,
            t.allen_electronegativity_difference,
            t.pauling_electronegativity_difference,
            t.omega,
            t.gamma,
            t.lambda_,
            t.valence_electron_concentration,
            t.ea_ratio,
            t.mixing_enthalpy,
            t.mixing_entropy,
            t.formation_enthalpy,
            t.min_formation_enthalpy,
        ]:
            result.append(self._fmt(item, ".2f"))
        result.append(str(t.melting_temperature))
        result.append(p.microstructure)
        for item in [
            p.model_1,
            p.model_2,
            p.model_3,
            p.model_4,
            p.model_5,
            p.model_6,
            p.model_7(),
            p.model_8,
        ]:
            result.append(item)
        return result

    def __str__(self) -> str:
        """Return a human-readable summary of all calculated properties.

        Returns:
            Multi-line report of thermodynamic values and model predictions.
        """
        t = self.thermo
        p = self.predictor
        return (
            f"{self.formula:=^48}\n"
            f"{'Density':25}: {self._fmt(t.density)} g/cm^3\n"
            f"{'Delta':25}: {self._fmt(t.atomic_size_difference)} %\n"
            f"{'Delta (CN12)':25}: {self._fmt(t.atomic_size_difference_cn12)} %\n"
            f"{'Delta Chi (Allen)':25}: {self._fmt(t.allen_electronegativity_difference)} %\n"
            f"{'Delta Chi (Pauling)':25}: {self._fmt(t.pauling_electronegativity_difference)} %\n"
            f"{'Omega':25}: {self._fmt(t.omega)}\n"
            f"{'Gamma':25}: {self._fmt(t.gamma)}\n"
            f"{'Lambda':25}: {self._fmt(t.lambda_)}\n"
            f"{'VEC':25}: {self._fmt(t.valence_electron_concentration)}\n"
            f"{'e/a':25}: {self._fmt(t.ea_ratio)}\n"
            f"{'Mixing Enthalpy':25}: {self._fmt(t.mixing_enthalpy)} kJ/mol\n"
            f"{'Mixing Entropy':25}: {self._fmt(t.mixing_entropy)} J/K.mol\n"
            f"{'Formation Enthalpy':25}: {self._fmt(t.formation_enthalpy)} meV/atom\n"
            f"{'Min. Formation Enthalpy':25}: {self._fmt(t.min_formation_enthalpy)} meV/atom\n"
            f"{'Max. Formation Enthalpy':25}: {self._fmt(t.max_formation_enthalpy)} meV/atom\n"
            f"{'Melting Temperature':25}: {self._fmt(t.melting_temperature, '>10')} K\n"
            f"{'Critical Temperature':25}: {self._fmt(t.critical_temperature)} K\n"
            f"{'Phi (BCC)':25}: {self._fmt(t.phi_bcc)}\n"
            f"{'Phi (FCC)':25}: {self._fmt(t.phi_fcc)}\n"
            f"{'Delta G_ss':25}: {self._fmt(t.delta_g_ss)} kJ/mol\n"
            f"{'Delta G_max':25}: {self._fmt(t.delta_g_max)} kJ/mol\n"
            f"{'F Parameter':25}: {self._fmt(t.f_parameter)}\n"
            f"\n{'Predictions':=^48}\n"
            f"{'Microstructure':25}:     {p.microstructure}\n"
            f"{'Model 1':25}:     {p.model_1} (Omega={self._fmt(t.omega, '.2f')}, Delta={self._fmt(t.atomic_size_difference, '.2f')})\n"
            f"{'Model 2':25}:     {p.model_2} (DeltaHmix={self._fmt(t.mixing_enthalpy, '.2f')}, Delta={self._fmt(t.atomic_size_difference, '.2f')})\n"
            f"{'Model 3':25}:     {p.model_3} (Gamma={self._fmt(t.gamma, '.2f')})\n"
            f"{'Model 4':25}:     {p.model_4} (Lambda={self._fmt(t.lambda_, '.2f')})\n"
            f"{'Model 5':25}:     {p.model_5} (Phi={self._fmt(t.phi, '.2f')})\n"
            f"{'Model 6':25}:     {p.model_6} (Hf_min={self._fmt(t.min_formation_enthalpy, '.2f')}, Hf_max={self._fmt(t.max_formation_enthalpy, '.2f')})\n"
            f"{'Model 7':25}:     {p.model_7()} (k1={self._fmt(p.model_7_k1(), '.2f')}, k1_cr={self._fmt(p.model_7_k1_critical(), '.2f')})\n"
            f"{'Model 8':25}:     {p.model_8} (F={self._fmt(t.f_parameter, '.2f')})\n"
        )
