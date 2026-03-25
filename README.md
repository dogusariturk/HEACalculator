<div align="center">
  <a href="https://github.com/dogusariturk/HEACalculator">
    <img src="https://user-images.githubusercontent.com/46679086/200971710-3ad2327e-6183-4ef9-b3b7-06a57f004e1a.png" alt="Logo" width="120" height="120">
  </a>

# HEACalculator

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3590318.svg)](https://doi.org/10.5281/zenodo.3590318)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/license/gpl-3-0)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platforms](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)

[![Tests](https://github.com/dogusariturk/HEACalculator/actions/workflows/tests.yml/badge.svg)](https://github.com/dogusariturk/HEACalculator/actions/workflows/tests.yml)
[![Lint](https://github.com/dogusariturk/HEACalculator/actions/workflows/lint.yml/badge.svg)](https://github.com/dogusariturk/HEACalculator/actions/workflows/lint.yml)

`HEACalculator` is a Python tool for calculating phenomenological parameters based on thermodynamics and physics to predict the formation of solid solutions in High Entropy Alloys (HEAs). It provides both a CLI (Typer) and GUI (PyQt5) interface.

<p>
  <a href="https://github.com/dogusariturk/HEACalculator/issues/new?labels=bug">Report a Bug</a> |
  <a href="https://github.com/dogusariturk/HEACalculator/issues/new?labels=enhancement">Request a Feature</a> |
  <a href="https://dogusariturk.github.io/HEACalculator">Documentation</a>
</p>

</div>

---

## Installation

> [!NOTE]
> GUI support requires PyQt5, which is an optional dependency. Install with the `[gui]` extra if needed.

```sh
# Recommended — using uv
uv add HEACalculator          # CLI only
uv add "HEACalculator[gui]"   # with GUI support

# Alternative — using pip
pip install HEACalculator
pip install "HEACalculator[gui]"
```

---

## Usage

### Command Line Interface

Run `HEACalculator` without arguments to display the help text.

![HEACalculator](https://user-images.githubusercontent.com/46679086/205514909-ab4930cd-2f5b-4d9c-9598-750c661d44db.png)

`HEACalculator search single <ALLOY>` calculates all parameters and predictions for the given alloy and prints results to stdout.

```sh
HEACalculator search single FeCoCrNi
```

![HEACalculator_SearchSingle](https://user-images.githubusercontent.com/46679086/205514947-ca25fb25-c726-4de9-a79b-1cccf354b4e3.png)

`HEACalculator search range` calculates all parameters and predictions for a composition range over a set of elements.

```sh
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5
```

![HEACalculator_SearchRange](https://user-images.githubusercontent.com/46679086/205514952-95dcb909-2147-4fcf-91df-4e0d1a1321dc.png)

Use `HEACalculator search csv <FILE>` to run batch calculations from a CSV file, or append `--csv` to the `range` command to redirect output to a file:

```sh
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5 --csv > results.csv
```

### Graphical User Interface

```sh
HEACalculator gui
```

![HEACalculator_GUI](https://user-images.githubusercontent.com/46679086/205514915-e4ce2dbf-4636-4639-b978-3a018183ba82.png)

1. Select elements from the periodic table
2. Enter at% values in the table
3. Click **Calculate**
4. Click **Save** to export results as CSV

---

## Features

- Property calculations
  - Density
  - Melting Temperature
  - Mixing Enthalpy [^1]
  - Mixing Entropy
  - Formation Enthalpy [^2]
  - Valence Electron Concentration (VEC)

- Parameters and predictions
  - Expected Microstructure [^3]
  - Delta Parameter (Atomic Size Difference) [^4]
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

---

## License

This project is licensed under the GNU GPLv3 License. See the [LICENSE](./LICENSE) file for details.

---

## Citation

If you use HEACalculator in your research, please cite the following:

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
