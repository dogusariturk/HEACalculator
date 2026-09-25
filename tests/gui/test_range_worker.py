"""Tests for RangeSearchWorker, the QThread that parallelizes range screening."""

import os

import pytest
from conftest import select_elements
from PyQt6 import QtCore

from HEACalculator.app import RangeSearchWorker

ROW = ["Fe50Ni50"] + [str(index) for index in range(1, 26)]

SIZING_CASES = [1, 10, 1000]


def _collect(qtbot, worker: RangeSearchWorker) -> tuple[list[list], list[int]]:
    """Run a worker to completion and capture everything it emits.

    Args:
        qtbot: The pytest-qt bot used to wait for the final signal.
        worker: The worker to start.

    Returns:
        The rows emitted via ``result_ready`` and the counts via ``finished_with_count``.
    """
    rows: list[list] = []
    counts: list[int] = []
    worker.result_ready.connect(rows.append)
    worker.finished_with_count.connect(counts.append)

    with qtbot.waitSignal(worker.finished, timeout=10000):
        worker.start()

    return rows, counts


@pytest.fixture
def worker_results(monkeypatch):
    """Return a factory that stubs the range worker with canned results.

    Returns:
        A callable taking a list of ``(row, error)`` tuples.
    """

    def _install(results: list[tuple[list | None, str | None]]) -> None:
        pending = list(results)

        def _worker(_formula: str) -> tuple[list | None, str | None]:
            return pending.pop(0) if pending else (None, "exhausted")

        monkeypatch.setattr("HEACalculator.utils._range_worker", _worker)

    return _install


class TestSignals:
    """Tests for the signals a stubbed worker emits."""

    def test_each_success_emits_one_result(self, qtbot, stub_process_pool, worker_results):
        """Every calculable alloy is forwarded to the main thread."""
        worker_results([(ROW, None), (ROW, None)])

        rows, _counts = _collect(qtbot, RangeSearchWorker(["Fe50Ni50", "Fe25Ni75"]))

        assert rows == [ROW, ROW]

    def test_failures_are_not_emitted(self, qtbot, stub_process_pool, worker_results):
        """Alloys the core cannot calculate produce no row."""
        worker_results([(ROW, None), (None, "missing data")])

        rows, counts = _collect(qtbot, RangeSearchWorker(["Fe50Ni50", "Sm50Fe50"]))

        assert rows == [ROW]
        assert counts == [1]

    def test_final_count_matches_the_successes(self, qtbot, stub_process_pool, worker_results):
        """finished_with_count reports how many rows were emitted."""
        worker_results([(ROW, None)] * 3)

        rows, counts = _collect(qtbot, RangeSearchWorker(["a", "b", "c"]))

        assert counts == [len(rows)] == [3]

    def test_all_failures_report_zero(self, qtbot, stub_process_pool, worker_results):
        """A fully failed screen still finishes cleanly."""
        worker_results([(None, "missing data")] * 2)

        rows, counts = _collect(qtbot, RangeSearchWorker(["a", "b"]))

        assert rows == []
        assert counts == [0]

    def test_results_arrive_on_the_main_thread(self, qtbot, stub_process_pool, worker_results):
        """Widgets are only ever touched from the GUI thread."""
        worker_results([(ROW, None)])
        worker = RangeSearchWorker(["Fe50Ni50"])
        threads: list[QtCore.QThread | None] = []
        worker.result_ready.connect(lambda _row: threads.append(QtCore.QThread.currentThread()))

        with qtbot.waitSignal(worker.finished, timeout=10000):
            worker.start()

        assert threads == [QtCore.QThread.currentThread()]


class TestExecutorSizing:
    """Tests for how the worker sizes its process pool."""

    @pytest.mark.parametrize("count", SIZING_CASES, ids=[f"{count}_alloys" for count in SIZING_CASES])
    def test_worker_count_is_capped_by_the_workload(self, qtbot, stub_process_pool, worker_results, count):
        """Never spawn more processes than there are alloys or CPUs."""
        worker_results([(ROW, None)] * count)

        _collect(qtbot, RangeSearchWorker([f"alloy{index}" for index in range(count)]))

        assert stub_process_pool.instances[0].max_workers == min(os.cpu_count() or 1, count)

    @pytest.mark.parametrize("count", SIZING_CASES, ids=[f"{count}_alloys" for count in SIZING_CASES])
    def test_chunksize_is_at_least_one(self, qtbot, stub_process_pool, worker_results, count):
        """Small workloads must not compute a zero chunk size."""
        worker_results([(ROW, None)] * count)

        _collect(qtbot, RangeSearchWorker([f"alloy{index}" for index in range(count)]))

        executor = stub_process_pool.instances[0]
        expected = max(1, count // ((executor.max_workers or 1) * 4))
        assert executor.chunksize == expected >= 1


class TestConstruction:
    """Tests for the worker's own setup."""

    def test_worker_is_a_qthread(self, batch_page):
        """The worker runs off the GUI thread."""
        assert isinstance(RangeSearchWorker([], parent=batch_page), QtCore.QThread)

    def test_worker_is_parented_to_its_page(self, batch_page):
        """Qt owns the worker, so it dies with the page."""
        assert RangeSearchWorker([], parent=batch_page).parent() is batch_page


class TestRealMultiprocessing:
    """End-to-end tests that spawn a real ProcessPoolExecutor."""

    def test_real_search_populates_the_results_tree(self, qtbot, batch_page):
        """A tiny real range screen fills the tree with calculated rows."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        batch_page.ui.startSpinBox.setValue(0.0)
        batch_page.ui.endSpinBox.setValue(100.0)
        batch_page.ui.stepSpinBox.setValue(25.0)

        qtbot.mouseClick(batch_page.ui.btnSearch, QtCore.Qt.MouseButton.LeftButton)
        qtbot.waitUntil(batch_page.ui.btnSearch.isEnabled, timeout=120_000)

        # The batch page builds formulas from float percentages, hence the ".0" suffixes.
        tree = batch_page.ui.resultsTreeWidget
        assert tree.topLevelItemCount() == 3
        expected = {"Fe25.0Ni75.0", "Fe50.0Ni50.0", "Fe75.0Ni25.0"}
        assert {tree.topLevelItem(row).text(0) for row in range(3)} == expected

    def test_real_search_enables_save(self, qtbot, batch_page):
        """A real screen that produced rows unlocks CSV export."""
        select_elements(qtbot, batch_page, "Fe", "Ni")
        batch_page.ui.stepSpinBox.setValue(50.0)

        qtbot.mouseClick(batch_page.ui.btnSearch, QtCore.Qt.MouseButton.LeftButton)
        qtbot.waitUntil(batch_page.ui.btnSearch.isEnabled, timeout=120_000)

        assert batch_page.ui.btnSave.isEnabled()
