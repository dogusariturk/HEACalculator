# Usage

HEACalculator provides two interfaces, a **command-line interface (CLI)** and a **graphical user interface (GUI)**, both backed by the same calculation core.

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

| Option | Default | Description |
|--------|---------|-------------|
| `--elements` | *(required)* | Space-separated list of element symbols |
| `--start` | `0` | Lowest atomic % for each element |
| `--end` | `100` | Highest atomic % for each element |
| `--step` | `5` | Composition step size (at%) |
| `--csv` | `False` | Export results as CSV to stdout (same 21-column format as `search csv`) |

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

**Output columns:** Formula, Density (g/cm^3), Delta (%), Omega, Gamma, Lambda, VEC, Mixing Enthalpy (kJ/mol), Mixing Entropy (J/K.mol), Formation Enthalpy (meV/atom), Min. Formation Enthalpy (meV/atom), Melting Temperature (K), Crystal Structure, Model 1–8.

**Example**

```bash
HEACalculator search csv alloys.csv
```

---

### `gui` - Graphical User Interface

Launch the PyQt5 desktop application:

```bash
HEACalculator gui
```

> **Note:** Requires `PyQt5`. Install with `pip install "HEACalculator[gui]"`.

![HEACalculator GUI](https://user-images.githubusercontent.com/46679086/205514915-e4ce2dbf-4636-4639-b978-3a018183ba82.png)

**Workflow:**

1. Select elements from the periodic table
2. Enter the desired at% values in the table at the corresponding cells
3. Click **Calculate**
4. Click **Save** to export results as a CSV file

---

## Python API

HEACalculator can be used directly as a Python library.

### Single alloy calculation

```python
from HEACalculator import HEACalculator

hea = HEACalculator("FeCoCrNi")

# Thermodynamic properties
print(hea.thermo.mixing_enthalpy)          # kJ/mol
print(hea.thermo.mixing_entropy)           # J/K·mol
print(hea.thermo.formation_enthalpy)       # meV/atom
print(hea.thermo.density)                  # g/cm³
print(hea.thermo.melting_temperature)      # K
print(hea.thermo.valence_electron_concentration)
print(hea.thermo.atomic_size_difference)   # %
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

### Composition unit converter

```python
from HEACalculator.core.converter import BatchCalculator

calc = BatchCalculator({"Fe": 25.0, "Co": 25.0, "Cr": 25.0, "Ni": 25.0})

wt  = calc.at_to_wt()   # atomic% → weight%
vol = calc.at_to_vol()  # atomic% → volume%
at  = calc.wt_to_at()   # weight% → atomic%
```

### Accessing element data directly

```python
from HEACalculator.data import Element, MixingEnthalpy, FormationEnthalpy

fe = Element("Fe")
print(fe.atomic_weight)    # 55.845
print(fe.melting_point)    # 1811 K
print(fe.atomic_radius)    # 126 pm

dH = MixingEnthalpy(("Fe", "Co"))       # kJ/mol
dHf = FormationEnthalpy(("Fe", "Co"))   # meV/atom
```
