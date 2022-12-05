<div align="center">
  <a href="https://github.com/dogusariturk/HEACalculator">
    <img src="https://user-images.githubusercontent.com/46679086/200971710-3ad2327e-6183-4ef9-b3b7-06a57f004e1a.png" alt="Logo" width="120" height="120">
  </a>

<h3 align="center">HEACalculator</h3>

  <p align="center">
    *HEACalculator* is a Python tool for calculating phenomenological parameters based on thermodynamics and physics in order to predict the formation of solid solutions in High Entropy Alloys (HEAs)
    <br />
    <img width="1171" src="https://user-images.githubusercontent.com/46679086/205514727-a6637cda-f727-430f-af8c-463350763818.png">
  </p>
</div>

<div align="center">
<a href="https://doi.org/10.5281/zenodo.3590319"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3590319.svg" alt="DOI"></a>
<img src="https://img.shields.io/github/license/dogusariturk/HEACalculator" alt="LICENSE">
<img alt="GitHub release" src="https://img.shields.io/github/v/release/dogusariturk/HEACalculator?include_prereleases">
</div>

# Table of Contents

- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
- [Usage](#usage)
  * [Command Line Interface](#prerequisites)
  * [Graphical User Interface](#installation)
- [Features](#features)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

## Getting Started

To get the *HEACalculator* local copy up and running, follow these simple steps:

### Prerequisites

The *HEACalculator* only requires the following packages:

  - numpy
  - PyQt5
  - Typer
       
### Installation

#### Clone the repo

   ```sh
   git clone https://github.com/dogusariturk/HEACalculator.git
   ```

#### Change Directory
   ```sh
   cd HEACalculator
   ```

#### Install virtualenv via pip
   ```sh
   pip install virtualenv
   ```

#### Create a virtual environment
   ```sh
   virtualenv venv
   ```

#### Activate the virtual environment
- For UNIX-based systems
  
  ```sh
  source bin/activate
  ```

- For Windows-based systems:
  
    - If using the default command prompt (```cmd```), type:
    ```
    .\venv\Scripts\activate
    ```
  
    - If using Windows PowerShell (```PS```), type:
    ```
    .\venv\Scripts\Activate.ps1
    ```

#### Install HEACalculator
   ```sh
   pip install .
   ```

## Usage

### Command Line Interface

Calling `HEACalculator` without any option/argument will show the help text.

![HEACalculator](https://user-images.githubusercontent.com/46679086/205514909-ab4930cd-2f5b-4d9c-9598-750c661d44db.png)

Currently, *HEACalculator* supports two different calculation methods.

- `HEACalculator search single <ALLOY>` calculates all parameters/predictions for the given ALLOY and exports the results to the stdout (i.e., terminal)

![HEACalculator_SearchSingle](https://user-images.githubusercontent.com/46679086/205514947-ca25fb25-c726-4de9-a79b-1cccf354b4e3.png)

- `HEACalculator search range` calculates all parameters/predictions for a given composition range of a given set of elements and exports results to the stdout (i.e., terminal) by default.

![HEACalculator_SearchRange](https://user-images.githubusercontent.com/46679086/205514952-95dcb909-2147-4fcf-91df-4e0d1a1321dc.png)

- `--csv` flag can be used with `HEACalculator search range` command to make Range Search function to export the results in CSV format to the stdout or redirected to a file using the `>` operator.

### Graphical User Interface


  ![HEACalculator_GUI](https://user-images.githubusercontent.com/46679086/205514915-e4ce2dbf-4636-4639-b978-3a018183ba82.png)

- Start Graphical User Interface (GUI)
   ```sh
   HEACalculator gui
   ```
  
- Select elements from the periodic table
- Enter the requested at% values in the table at the corresponding cell
- Click *Calculate* button
- Click *Save* button to save the calculated values as a CSV file

## Features

- Property calculations
  - Density
  - Melting Temperature
  - Mixing Enthalpy [^1]
  - Mixing Entropy
  - Formation Enthalpy [^2]
  - Valance Electron Concentration (VEC)


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
[^4]: S.S.Fang, X. S. Xiao, L. Xia, W. H. Li, Y. D. Dong,J. Non-Cryst. Solids 2003, 321, 120.
[^5]: Yang, X.; Zhang, Y. Mater. Chem. Phys. 2012, 132, 233–238.
[^6]: Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T.; Scr. Mater. 94 (2015) 28–31.
[^7]: Singh, A.K.; Kumar N.; Dwivedi A.; Subramaniam A.; Intermetallics 53 (2014) 112–119.
[^8]: S. Guo, Q. Hu, C. Ng, C.T. Liu, Intermetallics 41 (0) (2013) 96–103.
[^9]: Y.F. Ye, Q. Wang, J. Lu, C.T. Liu, Y. Yang, Scr. Mater. 104 (2015) 53–55.
[^10]: O.N. Senkov, D.B. Miracle, J. Alloys Compd. 658 (2016) 603–607.
[^11]: D.J.M. King, S.C. Middleburgh, A.G. McGregor, M.B. Cortie, Acta Mater. 104 (2016) 172–179.


## Roadmap

- Core
* [ ] Implement remaining prediction Models


- GUI

* [x] Implement Save function
* [ ] Include Error Message Box
* [ ] Include Range Search
* [ ] Include Batch Calculations
* [ ] Include Batch Converter
* [ ] Create Package for Windows, macOS, and Linux

## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

## Citation

If you use HEACalculator, we kindly ask you to cite the following publication:

* Doğuhan Sarıtürk. HEACalculator. (2019) doi:10.5281/zenodo.3590318

## Contact

Doguhan Sariturk - doguhan.sariturk@gmail.com

