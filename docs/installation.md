# Installation & Quick Start

## Requirements

- Python **3.10** or later
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

---

## Installing HEACalculator

### Using uv (recommended)

```bash
uv add HEACalculator          # CLI only
uv add "HEACalculator[gui]"   # with GUI support
```

### Using pip

```bash
pip install HEACalculator
pip install "HEACalculator[gui]"   # with GUI support
```

> **Note:** GUI support requires PyQt5, which is an optional dependency. Only install the `[gui]` extra if you intend to use the graphical interface.

---

## Installing from Source

If you don't have uv, install it first:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then clone and sync:

```bash
git clone https://github.com/dogusariturk/HEACalculator.git
cd HEACalculator

uv sync                   # Core dependencies (CLI only)
uv sync --group dev       # Core + development tools (ruff, pytest, pre-commit)
uv sync --extra gui       # Core + GUI support (PyQt5)
uv sync --extra docs      # Core + documentation dependencies (mkdocs-material)
```

Alternatively with pip:

```bash
git clone https://github.com/dogusariturk/HEACalculator.git
cd HEACalculator
pip install .
pip install ".[gui]"      # with GUI support
```

---

## Verifying the Installation

```bash
HEACalculator --help
```

Expected output:

```
Usage: HEACalculator [OPTIONS] COMMAND [ARGS]...

  A tool for calculating High-Entropy Alloy (HEA) specific parameters and
  solid-solution predictions.

Options:
  --help  Show this message and exit.

Commands:
  gui     Starts the HEACalculator Graphical User Interface (GUI).
  search  Parameter search commands
```

---

## Quick Start

Calculate all parameters for FeCoCrNi:

```bash
HEACalculator search single FeCoCrNi
```

Screen a composition range for Al-Ti-V:

```bash
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5
```

Run batch calculations from a CSV file:

```bash
HEACalculator search csv alloys.csv
```

Launch the GUI:

```bash
HEACalculator gui
```

---

## Pre-commit Hooks (development)

Install pre-commit hooks after cloning to enable automatic linting and formatting on every commit:

```bash
uv run pre-commit install
```

Hooks run `ruff` for linting and formatting.

---

## Citation

If you use `HEACalculator` in your research, please cite:

> Sarıtürk, D. (2019). HEACalculator. Zenodo. https://doi.org/10.5281/zenodo.3590318

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
