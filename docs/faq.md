# FAQ

---

## What formula notation is supported?

`HEACalculator` uses a flexible chemical formula parser that handles several common styles:

| Style                   | Example            | Notes                                   |
|-------------------------|--------------------|-----------------------------------------|
| Equimolar (symbol-only) | `FeCoCrNi`         | All elements treated as equal fractions |
| Explicit atom counts    | `Fe25Co25Cr25Ni25` | Counts are normalised internally        |
| Nested brackets         | `(FeCo)2CrNi`      | Parentheses with multipliers            |
| Mixed counts            | `Fe10Co20Cr30Ni40` | Any non-negative integer counts         |

Element symbols must start with an uppercase letter (`Fe`, not `fe`). Spaces inside the formula are not allowed.

---

## What happens when I don't specify atom fractions?

If you provide a formula without numeric counts (e.g. `FeCoCrNi`), all elements are assumed to be **equimolar**. Internally the formula is treated as `Fe1Co1Cr1Ni1` and the fractions are normalized to sum to 1.

---

## How many elements are supported?

There is no hard limit on the number of components. However:

- The mixing enthalpy and formation enthalpy databases cover a finite set of binary pairs. If a pair is missing, a `MissingMixingEnthalpyError` or `MissingFormationEnthalpyError` is raised.
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
- Model 6 evaluates formation enthalpies at $0.55\,T_m$.
- Model 7 defaults to an annealing temperature of $0.60\,T_m$ (configurable).

---

## Can I use HEACalculator as a Python library?

Yes. Install the package and import directly:

```python
from HEACalculator import HEACalculator

hea = HEACalculator("AlCoCrFeNi")
print(hea.thermo.mixing_enthalpy)
```

See the [Usage](usage.md) page for full examples.

---

## How do I cite HEACalculator?

If you use `HEACalculator` in your research, please cite:

> Doğuhan Sarıtürk. *HEACalculator*. (2019). doi:[10.5281/zenodo.3590318](https://doi.org/10.5281/zenodo.3590318)

??? quote "BibTeX"
    ```bibtex
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

---

## How do I build the documentation locally?

```bash
uv sync --extra docs
uv run mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
