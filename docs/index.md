<div align="center">
  <img src="https://user-images.githubusercontent.com/46679086/200971710-3ad2327e-6183-4ef9-b3b7-06a57f004e1a.png" alt="HEACalculator Logo" width="120" height="120">
  <h1>HEACalculator</h1>
  <p><em>A Python tool for calculating thermodynamic parameters and predicting solid solution formation in High Entropy Alloys</em></p>
  <p>
    <a href="https://doi.org/10.5281/zenodo.3590319"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3590319.svg" alt="DOI"></a>
    <img src="https://img.shields.io/github/license/dogusariturk/HEACalculator" alt="License">
    <img src="https://img.shields.io/github/v/release/dogusariturk/HEACalculator?include_prereleases" alt="Release">
    <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  </p>
</div>

---

![HEACalculator screenshot](https://user-images.githubusercontent.com/46679086/205514727-a6637cda-f727-430f-af8c-463350763818.png)

---

## What is HEACalculator?

`HEACalculator` is a Python tool for calculating phenomenological parameters based on thermodynamics and physics in order to predict the formation of solid solutions in High Entropy Alloys (HEAs).

It exposes both a **command-line interface** (CLI) powered by [Typer](https://typer.tiangolo.com/) and a **graphical user interface** (GUI) built with [PyQt5](https://riverbankcomputing.com/software/pyqt/), sharing the same calculation core.

---

## Features

**Property calculations**

- Density
- Melting Temperature
- Mixing Enthalpy ($\Delta H_{\text{mix}}$)
- Mixing Entropy ($\Delta S_{\text{mix}}$)
- Formation Enthalpy ($\Delta H_f$)
- Valence Electron Concentration (VEC)

**Structural parameters**

- Expected Microstructure (FCC / BCC / HCP)
- Atomic Size Difference ($\delta$)
- Omega ($\Omega$)
- Gamma ($\gamma$)
- Lambda ($\lambda$)

**Solid-solution formation prediction**

- 8 independent published models (Yang & Zhang, Guo, Wang, Singh, Ye, Troparevsky, Senkov & Miracle, King)

---

## Quick Start

```bash
pip install HEACalculator
HEACalculator search single FeCoCrNi
```

See [Installation & Quick Start](installation.md) for detailed setup instructions and [Usage](usage.md) for all available commands.
