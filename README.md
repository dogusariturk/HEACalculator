<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/dogusariturk/HEACalculator">
    <img src="https://user-images.githubusercontent.com/46679086/200971710-3ad2327e-6183-4ef9-b3b7-06a57f004e1a.png" alt="Logo" width="120" height="120">
  </a>

<h3 align="center">HEACalculator</h3>

  <p align="center">
    A Python tool for calculating High-Entropy Alloy (HEA) specific parameters
    <br />
  </p>
</div>

<div align="center">
<a href="https://doi.org/10.5281/zenodo.3590319"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3590319.svg" alt="DOI"></a>
<img src="https://img.shields.io/github/license/dogusariturk/HEACalculator" alt="LICENSE">
<img alt="GitHub release" src="https://img.shields.io/github/v/release/dogusariturk/HEACalculator?include_prereleases">
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
       <a href="#usage">Usage</a>
       <ul>
        <li><a href="#graphical-user-interface">Graphical User Interface</a></li>
        <li><a href="#command-line-interface">Command Line Interface</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Getting Started

To get the HEACalculator local copy up and running, follow these simple steps:

### Dependencies

The tool only requires the following packages:
  <ul>
    <li>numpy</li>
    <li>thermo</li>
    <li>PyQt5</li>
  </ul>
       
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dogusariturk/HEACalculator.git
   ```
   
2. Change Directory
   ```sh
   cd HEACalculator
   ```

3. Install virtualenv via pip
   ```sh
   pip install virtualenv
   ```
   
4. Create a virtual environment
   ```sh
   virtualenv venv
   ```
   
5. Activate the virtual environment
   - For UNIX-based systems:
          ```
          python -m pip install -r requirements.txt
          ```
   - For Windows-based systems:
          ```
          venv\Scripts\activate.bat
          ```
6. Install dependencies (for GUI)
   ```sh
   pip install -r requirements.txt
   ```
   
6. Install HEACalculator (for CLI)
   ```sh
   python setup.py install
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Graphical User Interface

<img width="1171" alt="Screen Shot 2022-11-10 at 03 30 15" src="https://user-images.githubusercontent.com/46679086/200972137-9be982e4-1d0f-49f3-9636-692de3ca841b.png">

1. Start Graphical User Interface from HEACalculator’s main directory
   ```sh
   python HEACalculator.py
   ```
   
2. Select elements from the periodic table
3. Enter the requested at% values in the table at the corresponding cell
4. Click Calculate

### Command Line Interface

1. Import HEACalculator
   ```python
   from HEACalculator.core.HEA import HEACalculator
   ```
   
2. Initialize HEACalculator Class with a string
   ```python
   HEACalculator(<alloy_name>)
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Doguhan Sariturk - doguhan.sariturk@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>
