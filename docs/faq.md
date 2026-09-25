# FAQ

---

## What formula notation is supported?

`HEACalculator` uses a flexible chemical formula parser that handles several common styles:

| Style                   | Example                        | Notes                                       |
|-------------------------|--------------------------------|---------------------------------------------|
| Equimolar (symbol-only) | `FeCoCrNi`                     | All elements treated as equal fractions     |
| Explicit atom counts    | `Fe25Co25Cr25Ni25`             | Counts are normalized internally            |
| Fractional counts       | `Al0.5CoCrFeNi`                | Decimal counts are allowed                  |
| Nested brackets         | `(FeCo)2CrNi` or `[FeCo]2CrNi` | Round or square brackets with multipliers   |
| Mixed counts            | `Fe10Co20Cr30Ni40`             | Any non-negative integer or decimal counts  |

Element symbols must start with an uppercase letter (`Fe`, not `fe`). Spaces are ignored, so `Fe Co Cr Ni` and `FeCoCrNi` are the same alloy. Quote a formula that contains spaces on the command line (e.g. `HEACalculator search single "Fe25 Co75"`), otherwise the shell splits it into separate arguments.

---

## What happens when I don't specify atom fractions?

If you provide a formula without numeric counts (e.g. `FeCoCrNi`), all elements are assumed to be **equimolar**. Internally the formula is treated as `Fe1Co1Cr1Ni1` and the fractions are normalized to sum to 1.

---

## How many elements are supported?

There is no hard limit on the number of components. However:

- The mixing enthalpy and formation enthalpy databases cover a finite set of binary pairs. If a pair is missing, the values that need it (and the models that use them) are reported as `N/A` (`null` in JSON), and everything else is still calculated. See [Some results show `N/A`](troubleshooting.md#some-results-show-na).
- Solid-solution criteria were derived for 5-component alloys and may be less reliable for 2- or 3-component systems.

---

## Which prediction model should I trust?

No single model is universally reliable across all alloy families. As a rule of thumb:

- **Model 1 (Yang & Zhang)** and **Model 2 (Guo *et al.*)** are the most widely cited and provide a good baseline.
- **Model 6 (Troparevsky *et al.*)** is based on DFT formation enthalpies and tends to be more physically grounded.
- **Model 8 (King *et al.*)** uses Gibbs free energy and is considered one of the more thermodynamically rigorous criteria.
- Use multiple models together: if several agree, confidence is higher.

---

## Does HEACalculator account for temperature effects?

Most parameters (density, VEC, delta, mixing enthalpy/entropy) are calculated at 0 K or use reference-temperature data. Exceptions:

- `omega` is evaluated at the estimated melting temperature $T_m$.
- `omega_at(T)` can be called with an arbitrary temperature.
- Model 6 compares the 0 K DFT formation enthalpies against the entropy bound $-T\,\Delta S_{\text{mix}}$, evaluated at $T = 0.55\,T_m$.
- Model 7 defaults to an annealing temperature of $0.55\,T_m$ and $k_2 = 0.6$; both can be changed with `model_7(k_2=..., annealing_temperature=...)`.

---

## Can I use HEACalculator as a Python library?

Yes. Install the package and import directly:

```python
from HEACalculator import HEACalculator

hea = HEACalculator("AlCoCrFeNi")
print(hea.thermo.mixing_enthalpy)
```

To calculate many alloys in parallel, use `HEACalculator.screen`. See [Parallel screening](usage.md#parallel-screening).

See the [Usage](usage.md) page for full examples.

---

## How do I cite HEACalculator?

If you use `HEACalculator` in your research, please cite the following:

> Sarıtürk, D., Kalay, Y. E., & Arróyave, R. (2026). HEACalculator: An Open-Source Python Tool for Thermodynamic Property Calculation and Solid Solution Prediction in High-Entropy Alloys. arXiv. https://doi.org/10.48550/arXiv.2606.19661

> Sarıtürk, D. (2019). HEACalculator. Zenodo. https://doi.org/10.5281/zenodo.3590318

??? quote "BibTeX"
    ```bibtex
    @misc{sariturk_2026_arxiv,
      author    = {Sarıtürk, Doğuhan and Kalay, Yunus Eren and Arróyave, Raymundo},
      title     = {{HEACalculator}: An Open-Source {Python} Tool for Thermodynamic Property Calculation and Solid Solution Prediction in High-Entropy Alloys},
      year      = 2026,
      publisher = {arXiv},
      doi       = {10.48550/arXiv.2606.19661},
      url       = {https://doi.org/10.48550/arXiv.2606.19661},
    }

    @software{sariturk_2019_3590318,
      author    = {Sarıtürk, Doğuhan},
      title     = {HEACalculator},
      year      = 2019,
      publisher = {Zenodo},
      doi       = {10.5281/zenodo.3590318},
      url       = {https://doi.org/10.5281/zenodo.3590318},
    }
    ```

You should also cite the original papers for any specific prediction models you rely on. See the [Overview](overview.md#references) page for the full reference list.

---

## What license is HEACalculator released under?

`HEACalculator` is distributed under the **GNU General Public License v3.0 or later** (GPL-3.0-or-later). See the [LICENSE](https://github.com/dogusariturk/HEACalculator/blob/master/LICENSE) file for details.

---

## How do I report a bug or request a feature?

Open an issue on GitHub: [github.com/dogusariturk/HEACalculator/issues](https://github.com/dogusariturk/HEACalculator/issues)
