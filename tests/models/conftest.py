"""Shared fixtures for the model validation modules."""

import math
import statistics

import pytest

from HEACalculator.core.composition import AlloyComposition
from HEACalculator.core.models import SolidSolutionPredictor
from HEACalculator.core.thermodynamics import HEAThermodynamics


@pytest.fixture
def thermo():
    """Return a factory for the thermodynamics object of an alloy.

    Returns:
        Callable taking a formula and returning its thermodynamic descriptors.
    """

    def _thermo(formula):
        return HEAThermodynamics(AlloyComposition(formula))

    return _thermo


@pytest.fixture
def predictor():
    """Return a factory for the solid-solution predictor of an alloy.

    Returns:
        Callable taking a formula and returning a predictor over that composition.
    """

    def _predictor(formula):
        composition = AlloyComposition(formula)
        return SolidSolutionPredictor(composition, HEAThermodynamics(composition))

    return _predictor


@pytest.fixture
def predictor_with_deltas():
    """Return a factory for a predictor whose two size differences are forced apart.

    Lets a test prove which of the two a criterion consumes.

    Returns:
        Callable taking a formula and the two values to substitute.
    """

    def _predictor_with_deltas(formula, *, plain, cn12):
        composition = AlloyComposition(formula)
        thermodynamics = HEAThermodynamics(composition)
        thermodynamics.__dict__["atomic_size_difference"] = plain
        thermodynamics.__dict__["atomic_size_difference_cn12"] = cn12
        return SolidSolutionPredictor(composition, thermodynamics)

    return _predictor_with_deltas


@pytest.fixture
def median_error():
    """Return a function giving the median error between computed and published values.

    Used by the tests that compare one radius convention against the other, where the
    assertion is which of two medians is smaller rather than an absolute threshold.

    Returns:
        Callable taking rows and two accessors, returning the median error.
    """
    return _median_error


@pytest.fixture
def assert_median_error():
    """Return a function asserting the median error stays under a bound.

    Returns:
        Callable performing the assertion.
    """

    def _assert(rows, computed, published, *, below, relative=False, floor=0.0, rows_compared=None, worst=None):
        errors = _collect(rows, computed, published, relative, floor)
        unit = "%" if relative else ""
        if rows_compared is not None:
            assert len(errors) >= rows_compared, f"only {len(errors)} of {len(rows)} rows compared"
        median = statistics.median(errors)
        assert median < below, f"median error {median:.4f}{unit} over {len(errors)} rows, expected below {below}{unit}"
        if worst is not None:
            assert max(errors) < worst, f"largest error {max(errors):.4f}{unit}, expected below {worst}{unit}"

    return _assert


@pytest.fixture
def assert_classification():
    """Return a function asserting a criterion reproduces the published phase labels.

    Recall is checked per class as well as overall, so a criterion cannot pass by returning
    the majority label.

    Returns:
        Callable performing the assertion.
    """

    def _assert(rows, predict, expected, *, overall, solid_solution, intermetallic, rows_scored=None):
        scored = {True: [0, 0], False: [0, 0]}
        for row in rows:
            want = expected(row)
            if want is None:
                continue
            verdict = predict(row)
            if verdict == "N/A":
                continue
            scored[want][1] += 1
            scored[want][0] += (verdict == "Solid Solution") == want

        correct = scored[True][0] + scored[False][0]
        total = scored[True][1] + scored[False][1]
        if rows_scored is not None:
            assert total >= rows_scored, f"only {total} rows scored, expected {rows_scored}"
        assert correct / total >= overall, f"overall {correct}/{total} = {correct / total:.0%}, expected {overall:.0%}"
        for want, name, bound in ((True, "solid solution", solid_solution), (False, "intermetallic", intermetallic)):
            hit, seen = scored[want]
            assert hit / seen >= bound, f"{name} recall {hit}/{seen} = {hit / seen:.0%}, expected {bound:.0%}"

    return _assert


def _collect(rows, computed, published, relative, floor):
    """Return the per-row errors, skipping rows the database cannot evaluate.

    Args:
        rows: Published rows to compare.
        computed: Callable taking a row and returning this package's value.
        published: Callable taking a row and returning the paper's value.
        relative: Express errors as a percentage of the published value.
        floor: Lower bound on the denominator when *relative*, for values near zero.

    Returns:
        One error per row that evaluates to a finite number.
    """
    errors = []
    for row in rows:
        value = computed(row)
        if value is None or not math.isfinite(value):
            continue
        target = published(row)
        errors.append(abs(value - target) / max(abs(target), floor) * 100 if relative else abs(value - target))
    return errors


def _median_error(rows, computed, published, *, relative=False, floor=0.0):
    """Return the median error between computed and published values.

    Args:
        rows: Published rows to compare.
        computed: Callable taking a row and returning this package's value.
        published: Callable taking a row and returning the paper's value.
        relative: Express errors as a percentage of the published value.
        floor: Lower bound on the denominator when *relative*, for values near zero.

    Returns:
        Median absolute error, or median relative error in percent when *relative*.
    """
    return statistics.median(_collect(rows, computed, published, relative, floor))
