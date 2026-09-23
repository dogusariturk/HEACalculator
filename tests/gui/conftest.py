"""Shared fixtures and helpers for the PyQt6 GUI test suite.

Every test in this package drives real widgets through ``pytest-qt``'s ``qtbot``
rather than mocking Qt, so that signal/slot wiring, ``blockSignals`` handling, and
cross-thread delivery are all exercised for real.
"""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from collections.abc import Callable, Iterable, Iterator
from pathlib import Path
from typing import Any

import pytest
from PyQt6 import QtCore, QtWidgets
from pytestqt.qtbot import QtBot

from HEACalculator.app import BatchCalculationsPage, HEACalculatorMainWindow, NotificationBar, ParametersPage


def element_button(page: QtWidgets.QWidget, symbol: str) -> QtWidgets.QPushButton:
    """Return the periodic-table button for an element symbol.

    Lookup is by ``text()`` rather than ``objectName()`` because app.py wires the
    buttons by their label, and one button is misnamed (``ebtnAnd`` carries the text
    ``"Nd"``; there is no ``ebtnNd``).

    Args:
        page: A page widget owning the periodic-table buttons.
        symbol: Chemical symbol shown on the button, e.g. ``"Fe"``.

    Returns:
        The matching checkable push button.

    Raises:
        LookupError: If no element button carries that symbol.
    """
    for button in page.findChildren(QtWidgets.QPushButton):
        if button.objectName().startswith("ebtn") and button.text() == symbol:
            return button
    raise LookupError(f"No element button for {symbol!r}")


def select_elements(qtbot: QtBot, page: QtWidgets.QWidget, *symbols: str) -> None:
    """Click each named element button on a page, toggling it.

    Args:
        qtbot: The pytest-qt bot used to deliver the clicks.
        page: A page widget owning the periodic-table buttons.
        symbols: Chemical symbols to click, in order.
    """
    for symbol in symbols:
        qtbot.mouseClick(element_button(page, symbol), QtCore.Qt.MouseButton.LeftButton)


def tree_rows(tree_widget: QtWidgets.QTreeWidget) -> list[list[str]]:
    """Read a results tree back as plain text rows.

    Args:
        tree_widget: The tree to read.

    Returns:
        One list of column strings per top-level row.
    """
    columns = range(tree_widget.columnCount())
    rows = []
    for index in range(tree_widget.topLevelItemCount()):
        item = tree_widget.topLevelItem(index)
        assert item is not None
        rows.append([item.text(column) for column in columns])
    return rows


def table_rows(table_widget: QtWidgets.QTableWidget) -> list[list[str]]:
    """Read a composition table back as plain text rows.

    Args:
        table_widget: The table to read.

    Returns:
        One list of column strings per row, with missing cells rendered as ``""``.
    """
    columns = range(table_widget.columnCount())
    rows = []
    for row in range(table_widget.rowCount()):
        cells = [table_widget.item(row, column) for column in columns]
        rows.append([cell.text() if cell is not None else "" for cell in cells])
    return rows


@pytest.fixture
def notification_bar(qtbot: QtBot) -> NotificationBar:
    """Return a real NotificationBar managed by qtbot.

    Returns:
        A freshly constructed notification bar.
    """
    bar = NotificationBar()
    qtbot.addWidget(bar)
    return bar


@pytest.fixture
def parameters_page(qtbot: QtBot) -> ParametersPage:
    """Return a real ParametersPage managed by qtbot.

    Returns:
        A freshly constructed parameters page.
    """
    page = ParametersPage()
    qtbot.addWidget(page)
    return page


@pytest.fixture
def batch_page(qtbot: QtBot) -> BatchCalculationsPage:
    """Return a real BatchCalculationsPage managed by qtbot.

    Returns:
        A freshly constructed batch calculations page.
    """
    page = BatchCalculationsPage()
    qtbot.addWidget(page)
    return page


@pytest.fixture
def main_window(qtbot: QtBot) -> HEACalculatorMainWindow:
    """Return a real HEACalculatorMainWindow managed by qtbot.

    Returns:
        A freshly constructed main window with both pages wired up.
    """
    window = HEACalculatorMainWindow()
    qtbot.addWidget(window)
    return window


class MessageBoxSpy:
    """Records how many times a patched QMessageBox.exec was invoked."""

    def __init__(self, answer: QtWidgets.QMessageBox.StandardButton) -> None:
        """Store the canned answer and reset the call counter.

        Args:
            answer: Standard button value returned from every ``exec()`` call.
        """
        self.answer = answer
        self.calls = 0

    def __call__(self, *args: Any) -> QtWidgets.QMessageBox.StandardButton:
        """Record the call and return the canned answer.

        Patched onto the QMessageBox class, this instance is not a descriptor, so
        ``box.exec()`` reaches it with no bound receiver.

        Args:
            args: Whatever ``exec()`` was called with; ignored.

        Returns:
            The canned standard button value.
        """
        self.calls += 1
        return self.answer


def _patch_message_box(monkeypatch: pytest.MonkeyPatch, answer: QtWidgets.QMessageBox.StandardButton) -> MessageBoxSpy:
    """Replace QMessageBox.exec with a spy returning a fixed answer.

    Args:
        monkeypatch: The pytest monkeypatch fixture.
        answer: Standard button value the patched ``exec()`` returns.

    Returns:
        The installed spy, for call-count assertions.
    """
    spy = MessageBoxSpy(answer)
    monkeypatch.setattr(QtWidgets.QMessageBox, "exec", spy)
    return spy


@pytest.fixture
def confirm_clear(monkeypatch: pytest.MonkeyPatch) -> MessageBoxSpy:
    """Make every confirmation dialog answer Yes.

    Returns:
        A spy recording how many dialogs were shown.
    """
    return _patch_message_box(monkeypatch, QtWidgets.QMessageBox.StandardButton.Yes)


@pytest.fixture
def cancel_clear(monkeypatch: pytest.MonkeyPatch) -> MessageBoxSpy:
    """Make every confirmation dialog answer No.

    Returns:
        A spy recording how many dialogs were shown.
    """
    return _patch_message_box(monkeypatch, QtWidgets.QMessageBox.StandardButton.No)


class SaveDialogSpy:
    """Records the arguments passed to a patched QFileDialog.getSaveFileName."""

    def __init__(self, result: tuple[str, bool]) -> None:
        """Store the canned dialog result.

        Args:
            result: ``(path, accepted)`` tuple returned from every call.
        """
        self.result = result
        self.calls: list[tuple[Any, ...]] = []

    def __call__(self, *args: Any, **kwargs: Any) -> tuple[str, bool]:
        """Record the call arguments and return the canned result.

        Args:
            args: Positional arguments the production code passed.
            kwargs: Keyword arguments the production code passed.

        Returns:
            The canned ``(path, accepted)`` tuple.
        """
        self.calls.append(args)
        return self.result


@pytest.fixture
def save_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Route the CSV save dialog to a temporary file and accept it.

    Returns:
        The path the dialog will hand back to the production code.
    """
    target = tmp_path / "results.csv"
    monkeypatch.setattr(QtWidgets.QFileDialog, "getSaveFileName", SaveDialogSpy((str(target), True)))
    return target


@pytest.fixture
def save_dialog_spy(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> SaveDialogSpy:
    """Route the CSV save dialog to a temporary file and expose the recorded arguments.

    Returns:
        The installed spy, for asserting the dialog's title, directory and filter.
    """
    spy = SaveDialogSpy((str(tmp_path / "results.csv"), True))
    monkeypatch.setattr(QtWidgets.QFileDialog, "getSaveFileName", spy)
    return spy


@pytest.fixture
def cancelled_save(monkeypatch: pytest.MonkeyPatch) -> SaveDialogSpy:
    """Make the CSV save dialog report that the user cancelled.

    Returns:
        The installed spy, for call-count assertions.
    """
    spy = SaveDialogSpy(("", False))
    monkeypatch.setattr(QtWidgets.QFileDialog, "getSaveFileName", spy)
    return spy


class FakeExecutor:
    """In-process stand-in for ProcessPoolExecutor used by RangeSearchWorker."""

    instances: list["FakeExecutor"] = []

    def __init__(self, max_workers: int | None = None) -> None:
        """Record the requested worker count.

        Args:
            max_workers: Worker count RangeSearchWorker asked for.
        """
        self.max_workers = max_workers
        self.chunksize: int | None = None
        FakeExecutor.instances.append(self)

    def __enter__(self) -> "FakeExecutor":
        """Enter the context manager.

        Returns:
            This executor.
        """
        return self

    def __exit__(self, *exc_info: object) -> bool:
        """Leave the context manager without suppressing exceptions.

        Args:
            exc_info: Standard exception triple, ignored.

        Returns:
            False, so exceptions propagate.
        """
        return False

    def map(self, fn: Callable[[str], Any], iterable: Iterable[str], chunksize: int = 1) -> Iterator[Any]:
        """Apply fn to every item in the current process.

        Args:
            fn: The worker callable RangeSearchWorker supplied.
            iterable: Alloy formula strings.
            chunksize: Chunk size RangeSearchWorker computed; recorded, not used.

        Returns:
            An iterator over the worker results.
        """
        self.chunksize = chunksize
        return iter([fn(item) for item in iterable])


@pytest.fixture
def stub_process_pool(monkeypatch: pytest.MonkeyPatch) -> type[FakeExecutor]:
    """Run range-search work in-process instead of spawning subprocesses.

    Returns:
        The FakeExecutor class, whose ``instances`` list records each construction.
    """
    FakeExecutor.instances = []
    monkeypatch.setattr("HEACalculator.app.ProcessPoolExecutor", FakeExecutor)
    return FakeExecutor
