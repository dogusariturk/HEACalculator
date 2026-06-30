<div align="center" markdown>

<img src="https://user-images.githubusercontent.com/46679086/200971710-3ad2327e-6183-4ef9-b3b7-06a57f004e1a.png" alt="Logo" width="200" height="200">

# HEACalculator

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/license/gpl-3-0)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platforms](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)

[![Tests](https://github.com/dogusariturk/HEACalculator/actions/workflows/tests.yml/badge.svg)](https://github.com/dogusariturk/HEACalculator/actions/workflows/tests.yml)
[![Lint](https://github.com/dogusariturk/HEACalculator/actions/workflows/lint.yml/badge.svg)](https://github.com/dogusariturk/HEACalculator/actions/workflows/lint.yml)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3590318.svg)](https://doi.org/10.5281/zenodo.3590318)
[![DOI](https://img.shields.io/badge/DOI-10.48550%2FarXiv.2606.19661-blue.svg)](https://doi.org/10.48550/arXiv.2606.19661)

`HEACalculator` is a Python tool for calculating phenomenological parameters based on thermodynamics and physics to predict the formation of solid solutions in High Entropy Alloys (HEAs).

<p>
  <a href="https://github.com/dogusariturk/HEACalculator/issues/new?labels=bug">Report a Bug</a> |
  <a href="https://github.com/dogusariturk/HEACalculator/issues/new?labels=enhancement">Request a Feature</a> |
  <a href="https://dogusariturk.github.io/HEACalculator">Documentation</a>
</p>

</div>

---

![HEACalculator screenshot](https://user-images.githubusercontent.com/46679086/205514727-a6637cda-f727-430f-af8c-463350763818.png)

---

## What is HEACalculator?

High Entropy Alloys (HEAs) are multi-principal-element alloys that are difficult to characterize from composition alone. `HEACalculator` takes a composition as input, computes thermodynamic and physical parameters, and runs those values through eight published solid-solution formation models.

A CLI (built on [Typer](https://typer.tiangolo.com/)) and a GUI (built with [PyQt6](https://riverbankcomputing.com/software/pyqt/)) both use the same calculation core.

---

## Features

**Property calculations**

- Density (g/cm$^3$)
- Melting Temperature (K)
- Mixing Enthalpy, $\Delta H_{\text{mix}}$ (kJ/mol)
- Miedema Mixing Enthalpy, $\Delta H_{\text{mix}}$ (kJ/mol)
- Mixing Entropy, $\Delta S_{\text{mix}}$ (J/K·mol)
- Formation Enthalpy, $\Delta H_f$ (meV/atom)
- Minimum Formation Enthalpy, min. $\Delta H_f$ (meV/atom)
- Valence Electron Concentration (VEC)
- Hume-Rothery Electron-to-Atom Ratio (e/a)

**Structural parameters**

- Atomic Size Difference, $\delta$ (%)
- Atomic Size Difference (CN12), $\delta_{\text{CN12}}$ (%)
- Electronegativity Difference, $\Delta\chi_{\text{Allen}}$ (%)
- Electronegativity Difference, $\Delta\chi_{\text{Pauling}}$ (%)
- Omega, $\Omega$
- Gamma, $\gamma$
- Lambda, $\lambda$
- Phi, $\phi$
- $\Delta G_{\text{SS}}$
- $\Delta G_{\text{max}}$

**Solid-solution formation prediction**

- Expected Microstructure (FCC / BCC / HCP / BCC+FCC)
- 8 independent published models (Yang & Zhang, Guo, Wang, Singh, Ye, Troparevsky, Senkov & Miracle, King)

---

## Quick Start

```bash
uvx HEACalculator search single FeCoCrNi
```

See [Installation & Quick Start](installation.md) for project installs, `uv` tool installs, and pip-based setups. See [Usage](usage.md) for command examples and the `uv` tool workflow.

---

## Citation

If you use `HEACalculator` in your research, please cite the following:

> Sarıtürk, D., Kalay, Y. E., & Arróyave, R. (2026). HEACalculator: An Open-Source Python Tool for Thermodynamic Property Calculation and Solid Solution Prediction in High-Entropy Alloys. arXiv. https://doi.org/10.48550/arXiv.2606.19661

> Sarıtürk, D. (2019). HEACalculator. Zenodo. https://doi.org/10.5281/zenodo.3590318

???+ quote "BibTeX"
    ```bibtex
    @misc{sariturk_2026_arxiv,
      author    = {Sarıtürk, Doğuhan and Kalay, Yunus Eren and Arróyave, Raymundo},
      title     = {{HEACalculator}: An Open-Source {Python} Tool for Thermodynamic Property Calculation and Solid Solution Prediction in High-Entropy Alloys},
      year      = 2026,
      publisher = {arXiv},
      doi       = {10.48550/arXiv.2606.19661},
      url       = {https://doi.org/10.48550/arXiv.2606.19661},
    }

    @software{sariturk_2019_3590318,
      author    = {Sarıtürk, Doğuhan},
      title     = {HEACalculator},
      year      = 2019,
      publisher = {Zenodo},
      doi       = {10.5281/zenodo.3590318},
      url       = {https://doi.org/10.5281/zenodo.3590318},
    }
    ```
