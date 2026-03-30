# Usage

`HEACalculator` provides two interfaces, a **command-line interface (CLI)** and a **graphical user interface (GUI)**, both backed by the same calculation core.

---

## Usage as a Tool

If you are using the `uv` tool workflow, you can run `HEACalculator` without adding it to a project's dependency list.

For a persistent installation managed by `uv`:

```bash
uv tool install HEACalculator
HEACalculator --help
HEACalculator search single FeCoCrNi
```

For a one-off invocation:

```bash
uvx HEACalculator search single FeCoCrNi
```

If you need the desktop GUI, install or run the package with the `gui` extra:

```bash
uv tool install "HEACalculator[gui]"
HEACalculator gui
```

Or run the GUI without installing permanently:

```bash
uvx --from "HEACalculator[gui]" HEACalculator gui
```

Use `uv add` instead when `HEACalculator` should live inside a project's environment as a dependency.

---

## Command-Line Interface

Running `HEACalculator` without arguments displays the help screen:

```bash
HEACalculator --help
```

![HEACalculator CLI help](https://user-images.githubusercontent.com/46679086/205514909-ab4930cd-2f5b-4d9c-9598-750c661d44db.png)

---

### `search single` - Single Alloy

Calculate all thermodynamic parameters and solid-solution predictions for a single alloy formula:

```bash
HEACalculator search single <ALLOY>
```

**Examples**

```bash
HEACalculator search single FeCoCrNi
HEACalculator search single Fe25Co25Cr25Ni25
HEACalculator search single "(FeCo)2CrNi"
```

The formula parser handles equimolar notation (`FeCoCrNi`), explicit atom counts (`Fe25Co25Cr25Ni25`), and nested bracket notation (`(FeCo)2CrNi`).

![search single output](https://user-images.githubusercontent.com/46679086/205514947-ca25fb25-c726-4de9-a79b-1cccf354b4e3.png)

---

### `search range` - Composition Range Screening

Screen all composition combinations within a given range for a set of elements:

```bash
HEACalculator search range --elements "El1 El2 ..." [OPTIONS]
```

**Options**

| Option       | Default      | Description                             |
|--------------|--------------|-----------------------------------------|
| `--elements` | *(required)* | Space-separated list of element symbols |
| `--start`    | `0`          | Lowest at% for each element             |
| `--end`      | `100`        | Highest at% for each element            |
| `--step`     | `5`          | Composition step size (at%)             |
| `--csv`      | `False`      | Export results as CSV to stdout         |

Pure single-element compositions (one element at 100 at%, the rest at 0 at%) are excluded from `search range` results, even when both `--start 0` and `--end 100` are used with a step that lands on those endpoints.

**Examples**

```bash
# Print results to terminal
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5

# Export to CSV file
HEACalculator search range --elements "Fe Co Cr Ni" --step 10 --csv > results.csv
```

![search range output](https://user-images.githubusercontent.com/46679086/205514952-95dcb909-2147-4fcf-91df-4e0d1a1321dc.png)

---

### `search csv` - Batch Calculation from CSV

Calculate HEA parameters for every composition listed in a CSV file:

```bash
HEACalculator search csv <FILE>
```

**CSV format requirements**

The input file must contain a column named `composition` (case-insensitive):

```
composition,note
FeCoCrNi,equimolar quaternary
Fe25Co25Cr25Ni25,same as above explicit
AlCoCrFeNi,quinary
```

Rows with missing or unparseable compositions are skipped and an error is printed to stderr.

**Output columns:** Formula, Density (g/cm^3), Delta (%), Delta (CN12) (%), Delta Chi (Allen) (%), Omega, Gamma, Lambda, VEC, Mixing Enthalpy (kJ/mol), Mixing Entropy (J/K.mol), Formation Enthalpy (meV/atom), Min. Formation Enthalpy (meV/atom), Melting Temperature (K), Crystal Structure, Model 1–8.

**Example**

```bash
HEACalculator search csv alloys.csv
```

---

### `gui` - Graphical User Interface

Launch the PyQt6 desktop application:

```bash
HEACalculator gui
```

> **Note:** Requires `PyQt6`. Install with `uv add "HEACalculator[gui]"` or `pip install "HEACalculator[gui]"`.

![HEACalculator GUI](https://user-images.githubusercontent.com/46679086/205514915-e4ce2dbf-4636-4639-b978-3a018183ba82.png)

The GUI has two pages, switched via the navigation buttons on the left:

**Parameters page (single alloy)**

1. Select elements from the periodic table (percentages are distributed equally by default)
2. Adjust the at% values in the composition table as needed
3. Click **Calculate**
4. Click **Save** to export results as a CSV file

**Batch Calculations page (range screening)**

Equivalent to the CLI `search range` command.

1. Select elements from the periodic table
2. Set the composition range and step size
3. Click **Search**
4. Click **Save** to export results as a CSV file

---

## Python API

`HEACalculator` can be used directly as a Python library.

### Single alloy calculation

```python
from HEACalculator import HEACalculator

hea = HEACalculator("FeCoCrNi")

# Thermodynamic properties
print(hea.thermo.mixing_enthalpy)               # kJ/mol
print(hea.thermo.mixing_entropy)                # J/K·mol
print(hea.thermo.formation_enthalpy)            # meV/atom
print(hea.thermo.density)                       # g/cm³
print(hea.thermo.melting_temperature)           # K
print(hea.thermo.valence_electron_concentration)
print(hea.thermo.atomic_size_difference)        # %
print(hea.thermo.atomic_size_difference_cn12)   # % (CN12-corrected radii)
print(hea.thermo.electronegativity_difference)  # % (Allen CE scale)
print(hea.thermo.omega)
print(hea.thermo.gamma)
print(hea.thermo.lambda_)

# Solid-solution predictions
print(hea.predictor.microstructure)        # "FCC", "BCC", "HCP", or "BCC+FCC"
print(hea.predictor.model_1)               # "Solid Solution" or "Intermetallic"
print(hea.predictor.model_2)
print(hea.predictor.model_3)
print(hea.predictor.model_4)
print(hea.predictor.model_5)
print(hea.predictor.model_6)
print(hea.predictor.model_7())             # method, accepts optional parameters
print(hea.predictor.model_8)

# Human-readable summary
print(hea)
```

### Omega at a specific temperature

```python
omega_800 = hea.thermo.omega_at(800)  # at 800 K
```

### Accessing element data directly

```python
from HEACalculator.data import Element, MixingEnthalpy, FormationEnthalpy

fe = Element("Fe")
print(fe.atomic_weight)             # 55.845
print(fe.melting_point)             # 1811 K
print(fe.atomic_radius)             # 126 pm
print(fe.allen_electronegativity)   # 1.80 (Pauling units)

dH = MixingEnthalpy(("Fe", "Co"))       # kJ/mol
dHf = FormationEnthalpy(("Fe", "Co"))   # meV/atom
```
