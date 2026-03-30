"""Facade class for High Entropy Alloy calculations."""

from __future__ import annotations

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.models import SolidSolutionPredictor
from HEACalculator.core.thermodynamics import HEAThermodynamics

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"
__version__ = "2.0.0"


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

    def __init__(self, formula: str) -> None:
        """Initialize with *formula*. All properties are computed lazily via ``thermo`` and ``predictor``."""
        self.formula = formula
        composition = AlloyComposition(formula)
        self.thermo = HEAThermodynamics(composition)
        self.predictor = SolidSolutionPredictor(composition, self.thermo)

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
            t.electronegativity_difference,
            t.omega,
            t.gamma,
            t.lambda_,
            t.valence_electron_concentration,
            t.mixing_enthalpy,
            t.mixing_entropy,
            t.formation_enthalpy,
            t.min_formation_enthalpy,
        ]:
            result.append(f"{item:.2f}")
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
            f"{'Density':25}: {t.density:>10.2f} g/cm^3\n"
            f"{'Delta':25}: {t.atomic_size_difference:>10.2f} %\n"
            f"{'Delta (CN12)':25}: {t.atomic_size_difference_cn12:>10.2f} %\n"
            f"{'Delta Chi (Allen)':25}: {t.electronegativity_difference:>10.2f} %\n"
            f"{'Omega':25}: {t.omega:>10.2f}\n"
            f"{'Gamma':25}: {t.gamma:>10.2f}\n"
            f"{'Lambda':25}: {t.lambda_:>10.2f}\n"
            f"{'VEC':25}: {t.valence_electron_concentration:>10.2f}\n"
            f"{'Mixing Enthalpy':25}: {t.mixing_enthalpy:>10.2f} kJ/mol\n"
            f"{'Mixing Entropy':25}: {t.mixing_entropy:>10.2f} J/K.mol\n"
            f"{'Formation Enthalpy':25}: {t.formation_enthalpy:>10.2f} meV/atom\n"
            f"{'Min. Formation Enthalpy':25}: {t.min_formation_enthalpy:>10.2f} meV/atom\n"
            f"{'Max. Formation Enthalpy':25}: {t.max_formation_enthalpy:>10.2f} meV/atom\n"
            f"{'Melting Temperature':25}: {t.melting_temperature:>10} K\n"
            f"{'Critical Temperature':25}: {t.critical_temperature:>10.2f} K\n"
            f"{'Phi (BCC)':25}: {t.phi_bcc:>10.2f}\n"
            f"{'Phi (FCC)':25}: {t.phi_fcc:>10.2f}\n"
            f"{'Delta G_ss':25}: {t.delta_g_ss:>10.2f} kJ/mol\n"
            f"{'Delta G_max':25}: {t.delta_g_max:>10.2f} kJ/mol\n"
            f"{'F Parameter':25}: {t.f_parameter:>10.2f}\n"
            f"\n{'Predictions':=^48}\n"
            f"{'Microstructure':25}:     {p.microstructure}\n"
            f"{'Model 1':25}:     {p.model_1} (Omega={t.omega:.2f}, Delta={t.atomic_size_difference:.2f})\n"
            f"{'Model 2':25}:     {p.model_2} (DeltaHmix={t.mixing_enthalpy:.2f}, Delta={t.atomic_size_difference:.2f})\n"
            f"{'Model 3':25}:     {p.model_3} (Gamma={t.gamma:.2f})\n"
            f"{'Model 4':25}:     {p.model_4} (Lambda={t.lambda_:.2f})\n"
            f"{'Model 5':25}:     {p.model_5} (Phi={t.phi:.2f})\n"
            f"{'Model 6':25}:     {p.model_6} (Hf_min={t.min_formation_enthalpy:.2f}, Hf_max={t.max_formation_enthalpy:.2f})\n"
            f"{'Model 7':25}:     {p.model_7()} (k1={p.model_7_k1():.2f}, k1_cr={p.model_7_k1_critical():.2f})\n"
            f"{'Model 8':25}:     {p.model_8} (F={t.f_parameter:.2f})\n"
        )
