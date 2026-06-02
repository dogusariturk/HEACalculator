<div align="center">

<img src="https://user-images.githubusercontent.com/46679086/200971710-3ad2327e-6183-4ef9-b3b7-06a57f004e1a.png" alt="Logo" width="200" height="200">

# HEACalculator

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/license/gpl-3-0)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platforms](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)

[![Tests](https://github.com/dogusariturk/HEACalculator/actions/workflows/tests.yml/badge.svg)](https://github.com/dogusariturk/HEACalculator/actions/workflows/tests.yml)
[![Lint](https://github.com/dogusariturk/HEACalculator/actions/workflows/lint.yml/badge.svg)](https://github.com/dogusariturk/HEACalculator/actions/workflows/lint.yml)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3590318.svg)](https://doi.org/10.5281/zenodo.3590318)

`HEACalculator` is a Python tool for calculating phenomenological parameters based on thermodynamics and physics to predict the formation of solid solutions in High Entropy Alloys (HEAs). It provides both a CLI (Typer) and GUI (PyQt6) interface.

<p>
  <a href="https://github.com/dogusariturk/HEACalculator/issues/new?labels=bug">Report a Bug</a> |
  <a href="https://github.com/dogusariturk/HEACalculator/issues/new?labels=enhancement">Request a Feature</a> |
  <a href="https://dogusariturk.github.io/HEACalculator">Documentation</a>
</p>

</div>

---

## Installation

> [!NOTE]
> GUI support requires PyQt6, which is an optional dependency. Install with the `[gui]` extra if needed.

Choose the workflow that matches how you want to use `HEACalculator`.

### Add to a Project with `uv`

Use this when `HEACalculator` should be installed inside a project's environment.

```sh
uv add HEACalculator
uv add "HEACalculator[gui]"
```

### Use as a Standalone Tool with `uv`

Use this when you want `uv` to manage `HEACalculator` as a CLI tool rather than a project dependency.

Persistent install:

```sh
uv tool install HEACalculator
HEACalculator --help
```

One-off run without installing permanently:

```sh
uvx HEACalculator search single FeCoCrNi
```

With GUI support:

```sh
uv tool install "HEACalculator[gui]"
HEACalculator gui
```
or
```sh
uvx --from "HEACalculator[gui]" HEACalculator gui
```

### Install with `pip`

Use this if you are not using `uv`.

```sh
pip install HEACalculator          # CLI only
pip install "HEACalculator[gui]"   # with GUI support
```

---

## Usage

### Command Line Interface

Run `HEACalculator` without arguments to display the help text.

![HEACalculator](https://user-images.githubusercontent.com/46679086/205514909-ab4930cd-2f5b-4d9c-9598-750c661d44db.png)

---

#### Single Alloy Calculations

![HEACalculator_SearchSingle](https://user-images.githubusercontent.com/46679086/205514947-ca25fb25-c726-4de9-a79b-1cccf354b4e3.png)

`HEACalculator search single <ALLOY>` calculates all parameters and predictions for the given alloy and prints results to stdout.

```sh
HEACalculator search single FeCoCrNi
```

Append `--json` to get a machine-readable JSON output with raw numeric values instead of formatted text:

```sh
HEACalculator search single FeCoCrNi --json
```

---

#### Range Screening

![HEACalculator_SearchRange](https://user-images.githubusercontent.com/46679086/205514952-95dcb909-2147-4fcf-91df-4e0d1a1321dc.png)


`HEACalculator search range` calculates all parameters and predictions for a composition range over a set of elements. Compositions are evaluated in parallel across all available CPU cores, so large screens complete significantly faster.

```sh
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5
```

Append `--csv` / `--json` to redirect output to a file:

```sh
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5 --csv > results.csv
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5 --json > results.ndjson
```

---

#### CSV Batch Calculations

`HEACalculator search csv <FILE>` calculates all parameters and predictions for every alloy listed in a CSV file.

> [!IMPORTANT]
> The input CSV file must contain a column named **`composition`**. Each row in that column should be a valid alloy formula (e.g. `FeCoCrNi`). Any other columns in the file are ignored.

```sh
HEACalculator search csv alloys.csv
```

Append `--json` to get machine-readable JSON output instead of formatted text:

```sh
HEACalculator search csv alloys.csv --json
```

### Graphical User Interface

```sh
HEACalculator gui
```

The GUI has two pages, switched via the navigation buttons on the left:

---

#### Parameters page (single alloy)

<img width="2342" height="1292" alt="HEACalculator_GUI-Parameters" src="https://github.com/user-attachments/assets/d13744ee-b60f-4922-a758-53b89876a7f5" />

1. Select elements from the periodic table (percentages are distributed equally by default)
2. Adjust the at% values in the composition table as needed
3. Click **Calculate**
4. Click **Save** to export results as CSV

---

#### Batch Calculations page (range screening)

<img width="2342" height="1292" alt="HEACalculator_GUI-RangeSearch" src="https://github.com/user-attachments/assets/f829e67b-c069-4857-9b13-56068f63f816" />

Equivalent to `search range`.

1. Select elements from the periodic table
2. Set the composition range and step size
3. Click **Search**
4. Click **Save** to export results as CSV

---

## Features

- Property calculations
  - Density
  - Melting Temperature
  - Mixing Enthalpy [^1]
  - Miedema Mixing Enthalpy [^11]
  - Mixing Entropy
  - Formation Enthalpy [^2]
  - Valence Electron Concentration (VEC)
  - Hume-Rothery Electron-to-Atom Ratio (e/a) [^17]

- Parameters and predictions
  - Expected Microstructure [^3]
  - Delta Parameter (Atomic Size Difference) [^4]
  - Delta Parameter (CN12-corrected Atomic Size Difference) [^4]
  - Electronegativity Difference (Allen CE scale)
  - Electronegativity Difference (Pauling scale) [^16]
  - Omega Parameter [^5]
  - Gamma Parameter [^6]
  - Lambda Parameter [^7]
  - Solid Solution Prediction Models
      - Model 1 [^5]
      - Model 2 [^8]
      - Model 3 [^6]
      - Model 4 [^7]
      - Model 5 [^9]
      - Model 6 [^2]
      - Model 7 [^10]
      - Model 8 [^11]

[^1]: Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. Prog. Mater. Sci. 2014, 61.
[^2]: Troparevsky, M. C.; Morris, J. R.; Kent, P. R. C.; Lupini, A. R.; Stocks, G. M.; Phys. Rev. X, 5(1) (2015)
[^3]: Guo, S.; Ng, C.; Lu, J.; Liu, C.T. J. Appl. Phys. 2011, 109, 103505.
[^4]: S.S.Fang, X. S. Xiao, L. Xia, W. H. Li, Y. D. Dong, J. Non-Cryst. Solids 2003, 321, 120.
[^5]: Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233–238.
[^6]: Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T.; Scr. Mater. 94 (2015) 28–31.
[^7]: Singh, A.K.; Kumar N.; Dwivedi A.; Subramaniam A.; Intermetallics 53 (2014) 112–119.
[^8]: S. Guo, Q. Hu, C. Ng, C.T. Liu, Intermetallics 41 (0) (2013) 96–103.
[^9]: Y.F. Ye, Q. Wang, J. Lu, C.T. Liu, Y. Yang, Scr. Mater. 104 (2015) 53–55.
[^10]: O.N. Senkov, D.B. Miracle, J. Alloys Compd. 658 (2016) 603–607.
[^11]: D.J.M. King, S.C. Middleburgh, A.G. McGregor, M.B. Cortie, Acta Mater. 104 (2016) 172–179.
[^16]: Haynes, W.M. CRC Handbook of Chemistry and Physics, 95th ed.; CRC Press: London, 2014. ISBN 9781482208689.
[^17]: Hume-Rothery, W.; Smallman, R.E.; Haworth, C.W. The Structure of Metals and Alloys, 5th ed.; Institute of Metals: London, 1969.

---

## License

This project is licensed under the GNU GPLv3 License. See the [LICENSE](https://github.com/dogusariturk/HEACalculator/blob/master/LICENSE) file for details.

---

## Citation

We are currently preparing a preprint for publication. If you use `HEACalculator` in your research, please cite the following:

> Sarıtürk, D. (2019). HEACalculator. Zenodo. https://doi.org/10.5281/zenodo.3590318

BibTeX:

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
