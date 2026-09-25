# Troubleshooting

---

## GUI won't launch

**Symptom**

```
ModuleNotFoundError: No module named 'PyQt6'
```

**Fix**

PyQt6 is an optional dependency and is not installed by default. Reinstall with the `gui` extra, using the command that matches how you installed `HEACalculator`:

=== "uv tool"

    If you installed `HEACalculator` as a standalone CLI tool with `uv tool install`:

    ```bash
    uv tool install "HEACalculator[gui]"
    ```

=== "uv add"

    If `HEACalculator` is a dependency in your project's environment:

    ```bash
    uv add "HEACalculator[gui]"
    ```

=== "pip"

    If you installed `HEACalculator` with `pip`:

    ```bash
    pip install "HEACalculator[gui]"
    ```

For a one-off run without installing, use `uvx --from "HEACalculator[gui]" HEACalculator gui`.

---

## GUI won't launch on Linux (missing EGL library)

**Symptom**

```
ImportError: libEGL.so.1: cannot open shared object file: No such file or directory
```

**Cause**

PyQt6 requires EGL to initialize its rendering backend. On minimal Linux installations (e.g. CI runners, headless servers, or fresh Docker containers), the `libegl1` system package may not be present.

**Fix**

Install the missing system library via your package manager:

```bash
# Debian / Ubuntu
sudo apt-get install -y libegl1
```

After installing, retry `HEACalculator gui`.

---

## ElementNotFoundError

**Symptom**

```
ElementNotFoundError: "Element not found in database: 'E'"
```

**Cause**

The formula contains an element symbol that does not exist in the built-in element database. This usually means a typo in the formula. For example, in `FECoCrNi` the `FE` is read as `F` followed by `E`, and `E` is not an element.

**Fix**

Check that all element symbols are correctly capitalized (e.g. `Fe`, not `FE`) and that they correspond to real chemical elements. A symbol that starts with a lowercase letter, such as `fe`, gives a [formula parsing error](#formula-parsing-errors) instead.

```bash
# Wrong
HEACalculator search single FECoCrNi

# Correct
HEACalculator search single FeCoCrNi
```

---

## Some results show `N/A`

**Symptom**

```
Formation Enthalpy       :        N/A meV/atom
Model 6                  :     N/A (Hf_min=N/A, Hf_max=N/A)
```

In JSON output and `get_dict()`, the affected numbers are `null` (`None`) and the affected models are `"N/A"`.

**Cause**

A value needs data that is missing for at least one element or element pair in the alloy. `HEACalculator` reports that value, and every model that depends on it, as `N/A` and still calculates everything else. The binary formation enthalpies from the Troparevsky DFT dataset cover far fewer pairs than the mixing enthalpies, so formation enthalpy and Models 6 and 7 are the most common to show `N/A` (e.g. for any alloy that contains both Fe and Si).

**Fix**

The other results are unaffected and can be used as usual. To check whether a specific pair is covered, look it up directly; a missing pair raises an error:

```python
from HEACalculator.data import FormationEnthalpy

FormationEnthalpy(("Fe", "Si"))  # MissingFormationEnthalpyError: "No formation enthalpy data for pair ('Fe', 'Si')"
```

`MixingEnthalpy` works the same way and raises `MissingMixingEnthalpyError`. If you need coverage for additional pairs, consider contributing data to the project.

---

## `search csv`: missing or wrong column name

**Symptom**

```
No 'composition' column found in alloys.csv. Available columns: Alloy, description
```

**Cause**

The CSV file does not have a column named `composition` (case-insensitive match). The column may be named differently (e.g. `Alloy`, `Formula`).

**Fix**

Either rename the column in your CSV to `composition`, or point to the existing column with `--column`. For example, given this `alloys.csv`:

```csv
Alloy,description
FeCoCrNi,quaternary equimolar
AlCoCrFeNi,quinary
```

The compositions are in the `Alloy` column, so pass that name to `--column`:

```sh
HEACalculator search csv alloys.csv --column Alloy
```

Rows with empty or unparseable values in the composition column are skipped automatically.

---

## Formula parsing errors

**Symptom**

```
ValueError: Input may not be a formula; unrecognized characters were detected
```

**Cause**

The formula string cannot be parsed. The end of the message tells you why:

| Message ends with                           | Cause                                                                              | Example                         |
|---------------------------------------------|------------------------------------------------------------------------------------|---------------------------------|
| `unrecognized characters were detected`     | A symbol starts lowercase, or a character is not a symbol, count, bracket or space | `feCoCrNi`, `FeCocrNi`, `Fe-Co` |
| `unbalanced brackets`                       | An opening or closing bracket has no partner                                       | `(FeCo2CrNi`, `FeCo)2`          |
| `a count must follow an element or bracket` | A number appears before any element or bracket                                     | `2FeCo`                         |
| `no element has a nonzero count`            | Every element has a count of zero                                                  | `Fe0Co0`                        |

**Fix**

Use one of the supported notation styles:

| Style                 | Example                        |
|-----------------------|--------------------------------|
| Equimolar (no counts) | `FeCoCrNi`                     |
| Explicit atom counts  | `Fe25Co25Cr25Ni25`             |
| Fractional counts     | `Fe0.5CoCrNi`                  |
| Nested brackets       | `(FeCo)2CrNi` or `[FeCo]2CrNi` |

For `search range`, pass elements as a space-separated list via `--elements "Fe Co Cr Ni"`.

---

## Unexpected results for asymmetric compositions

The `search single` command accepts any valid formula. If no atom counts are specified, all elements are treated as **equimolar**. To specify custom fractions, use explicit counts:

```bash
HEACalculator search single Fe10Co30Cr30Ni30
```
