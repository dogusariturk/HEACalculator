# Contributing to HEACalculator

Thanks for your interest in improving `HEACalculator`. This guide walks through setting up a development environment and the checks your changes should pass before you open a pull request.

## Getting started

`HEACalculator` uses [uv](https://docs.astral.sh/uv/) for dependency management and packaging.

```sh
git clone https://github.com/dogusariturk/HEACalculator.git
cd HEACalculator
uv sync --all-extras --dev
```

This creates a `.venv` with the runtime, GUI, docs, and dev dependency groups installed. Prefix commands with `uv run` (e.g. `uv run pytest`), or activate the virtualenv directly.

Install the git hooks so lint and formatting checks run automatically on commit:

```sh
uv run prek install
```

## Development workflow

1. Create a branch off `master` for your change.
2. Make your change, keeping it focused and consistent with the surrounding code.
3. Add or update tests under `tests/` for any behavior change.
4. Update documentation under `docs/` if you change public APIs or CLI behavior.
5. Run the checks below before opening a pull request.

### Running tests

```sh
uv run pytest tests/ -v
```

Tests run against Python 3.10 through 3.14 on Linux, Windows, and macOS in CI (see `.github/workflows/tests.yml`); running locally on whatever interpreter uv picks up is fine.

### Linting, formatting, and type checking

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting and [ty](https://github.com/astral-sh/ty) for type checking, wired together with [prek](https://github.com/j178/prek):

```sh
uv run prek run --all-files
```

You can also run the tools individually:

```sh
uv run ruff check --fix .
uv run ruff format .
uvx ty check
```

If you installed the git hooks with `prek install`, these run automatically on `git commit`.

### Building the docs

Documentation lives in `docs/` and is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/):

```sh
uv run --extra docs mkdocs serve
```

## Code style

- Run `ruff format` before committing; it settles formatting questions (double quotes, spaces) so you don't have to think about them.
- Public functions, classes, and modules should have Google-style docstrings (enforced by ruff's pydocstyle rules).
- Prefer `pathlib` over `os.path`, and keep new code fully type-hinted.
- Keep the CLI (`src/HEACalculator/cli.py`) and GUI (`src/HEACalculator/gui/`) as thin wrappers around the core calculation logic in `src/HEACalculator/core/`.

## Commit messages and pull requests

- Write clear, imperative commit messages (e.g. "Add BSF k-path validation", not "Added" or "Adding").
- Keep pull requests focused on a single change; unrelated fixes should be separate PRs.
- Reference related issues in the PR description (e.g. `Fixes #123`).
- Ensure `uv run prek run --all-files` and `uv run pytest tests/ -v` pass locally before opening the PR. CI runs the same checks (`.github/workflows/lint.yml` and `.github/workflows/tests.yml`) and must pass before merge.

## Reporting bugs and requesting features

Please use the GitHub issue tracker:

- [Report a bug](https://github.com/dogusariturk/HEACalculator/issues/new?labels=bug)
- [Request a feature](https://github.com/dogusariturk/HEACalculator/issues/new?labels=enhancement)

Include a minimal reproducible example when reporting a bug, ideally with the element composition and settings that trigger the issue.

## License

By contributing, you agree that your contributions will be licensed under the project's [GPL-3.0-or-later license](LICENSE).
