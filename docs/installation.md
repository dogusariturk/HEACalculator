# Installation & Quick Start

## Requirements

- Python **3.10** or later
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

---

## Installing HEACalculator

> **Note:** GUI support requires PyQt6, which is an optional dependency. Install with the `[gui]` extra only if you intend to use the graphical interface.

Choose the workflow that matches how you want to use `HEACalculator`.

### Add to a Project with `uv`

Use this when `HEACalculator` should be installed inside a project's environment.

```bash
uv add HEACalculator          # CLI only
uv add "HEACalculator[gui]"   # with GUI support
```

### Use as a Standalone Tool with `uv`

Use this when you want `uv` to manage `HEACalculator` as a CLI tool rather than a project dependency.

Persistent install:

```bash
uv tool install HEACalculator
HEACalculator --help
```

One-off run without installing permanently:

```bash
uvx HEACalculator search single FeCoCrNi
```

With GUI support:

```bash
uv tool install "HEACalculator[gui]"
HEACalculator gui
```

Or run the GUI without installing permanently:

```bash
uvx --from "HEACalculator[gui]" HEACalculator gui
```

### Install with `pip`

Use this if you are not using `uv`.

```bash
pip install HEACalculator          # CLI only
pip install "HEACalculator[gui]"   # with GUI support
```

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
uv sync --group dev       # Core + development tools (ruff, pytest, prek, ty)
uv sync --extra gui       # Core + GUI support (PyQt6)
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

???+ quote "BibTeX"
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
