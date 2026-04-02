# Troubleshooting

---

## GUI won't launch

**Symptom**

```
ModuleNotFoundError: No module named 'PyQt6'
```

**Fix**

PyQt6 is an optional dependency and is not installed by default. Install it with:

```bash
uv add "HEACalculator[gui]"
# or with pip:
pip install "HEACalculator[gui]"
```

---

## GUI won't launch on Linux (missing EGL library)

**Symptom**

```
ImportError: libEGL.so.1: cannot open shared object file: No such file or directory
```

**Cause**

PyQt6 requires EGL (Embedded-Process Graphics Library) to initialize its rendering backend. On minimal Linux installations (e.g. CI runners, headless servers, or fresh Docker containers), the `libegl1` system package may not be present.

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
HEACalculator.exceptions.ElementNotFoundError: 'Xx'
```

**Cause**

The formula contains an element symbol that does not exist in the built-in element database. This usually means a typo in the formula.

**Fix**

Check that all element symbols are correctly capitalized (e.g. `Fe`, not `fe` or `FE`) and that they correspond to real chemical elements.

```bash
# Wrong
HEACalculator search single FeCocrNi

# Correct
HEACalculator search single FeCoCrNi
```

---

## MissingMixingEnthalpyError / MissingFormationEnthalpyError

**Symptom**

```
HEACalculator.exceptions.MissingMixingEnthalpyError: ('Fe', 'Xx')
```

**Cause**

The binary pair database does not contain an entry for the requested element pair. This can happen for rare or radioactive elements not covered by Miedema's model or the Troparevsky DFT dataset.

**Fix**

Use only element pairs that are present in the respective databases. If you need coverage for additional pairs, consider contributing data to the project.

---

## `search csv`: missing or wrong column name

**Symptom**

```
KeyError: 'composition'
```

**Cause**

The CSV file does not have a column named `composition` (case-insensitive match). The column may be named differently (e.g. `Alloy`, `Formula`).

**Fix**

Rename the column in your CSV to `composition`:

```csv
composition,description
FeCoCrNi,quaternary equimolar
AlCoCrFeNi,quinary
```

Rows with empty or unparseable values in the `composition` column are skipped automatically.

---

## Formula parsing errors

**Symptom**

```
ValueError: Invalid formula
```

**Cause**

The formula string cannot be parsed. Common causes:

- Unmatched parentheses: `(FeCo2CrNi`
- Lowercase element start: `feCoCrNi`
- Unknown characters or spaces: `Fe Co Cr Ni`

**Fix**

Use one of the supported notation styles:

| Style                 | Example            |
|-----------------------|--------------------|
| Equimolar (no counts) | `FeCoCrNi`         |
| Explicit atom counts  | `Fe25Co25Cr25Ni25` |
| Nested brackets       | `(FeCo)2CrNi`      |

Spaces are not allowed inside the formula string. For `search range`, pass elements as a space-separated list via `--elements "Fe Co Cr Ni"`.

---

## Unexpected results for asymmetric compositions

The `search single` command accepts any valid formula. If no atom counts are specified, all elements are treated as **equimolar**. To specify custom fractions, use explicit counts:

```bash
HEACalculator search single Fe10Co30Cr30Ni30
```
