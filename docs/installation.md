# Installation & Quick Start

## Requirements

- Python **3.10** or later
- pip or [uv](https://docs.astral.sh/uv/) (recommended)

---

## Installing HEACalculator

### Core install (CLI only)

```bash
pip install HEACalculator
```

This installs the CLI and all required dependencies (`numpy`, `pandas`, `typer`).

### With GUI support

The graphical user interface requires PyQt5, which is an optional extra:

```bash
pip install "HEACalculator[gui]"
```

### From source

```bash
git clone https://github.com/dogusariturk/HEACalculator.git
cd HEACalculator
pip install .
```

With GUI:

```bash
pip install ".[gui]"
```

---

## Installing with uv (recommended for development)

[uv](https://docs.astral.sh/uv/) is a fast Python package manager. If you don't have it, install it first:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then:

```bash
git clone https://github.com/dogusariturk/HEACalculator.git
cd HEACalculator

# Core dependencies
uv sync

# Core + development tools (ruff, pytest, pre-commit)
uv sync --group dev

# With GUI support
uv sync --extra gui

# With documentation dependencies
uv sync --extra docs
```

---

## Verifying the Installation

```bash
HEACalculator --help
```

You should see output similar to:

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

Calculate all parameters for FeCoCrNi in one command:

```bash
HEACalculator search single FeCoCrNi
```

Screen a composition range for Al-Ti-V:

```bash
HEACalculator search range --elements "Al Ti V" --start 0 --end 100 --step 5
```

Calculate parameters from a CSV file:

```bash
HEACalculator search csv alloys.csv
```

Launch the GUI:

```bash
HEACalculator gui
```

---

## Pre-commit Hooks (development)

If you are contributing to the project, install the pre-commit hooks after cloning:

```bash
uv run pre-commit install
```

Hooks run `ruff` for linting and formatting on every commit.
