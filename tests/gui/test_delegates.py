"""Tests for the item delegates and shared results-tree header configuration."""

import pytest
from PyQt6 import QtCore, QtGui, QtWidgets

from HEACalculator.app import AlignDelegate, BatchAmountDelegate, ItemDelegate, configure_results_tree_header

INTERACTIVE_COLUMN = 7

_ACCEPTABLE = QtGui.QValidator.State.Acceptable
_INTERMEDIATE = QtGui.QValidator.State.Intermediate
_INVALID = QtGui.QValidator.State.Invalid

# Qt distinguishes two kinds of rejection: Invalid refuses the keystroke outright,
# while Intermediate lets the text sit in the editor but blocks the commit.
AMOUNT_VALIDATION_CASES = [
    ("50.5", _ACCEPTABLE),
    ("0", _ACCEPTABLE),
    ("100", _ACCEPTABLE),
    ("100.000", _ACCEPTABLE),
    ("150", _INTERMEDIATE),
    ("50.1234", _INVALID),
    ("-1", _INVALID),
    ("abc", _INVALID),
]

BATCH_VALIDATION_CASES = [
    ("0.5", _ACCEPTABLE),
    ("1234.5678", _ACCEPTABLE),
    ("999999", _ACCEPTABLE),
    ("0", _INTERMEDIATE),
    ("1000000", _INTERMEDIATE),
    ("-5", _INVALID),
    ("abc", _INVALID),
]


def _make_editor(delegate: QtWidgets.QStyledItemDelegate, parent: QtWidgets.QWidget) -> QtWidgets.QWidget | None:
    """Build an editor widget from a delegate with throwaway option/index arguments.

    Args:
        delegate: The delegate under test.
        parent: Widget to parent the editor to.

    Returns:
        The editor widget the delegate created, or None if it declined to make one.
    """
    return delegate.createEditor(parent, QtWidgets.QStyleOptionViewItem(), QtCore.QModelIndex())


def _make_validator(delegate: QtWidgets.QStyledItemDelegate, parent: QtWidgets.QWidget) -> QtGui.QDoubleValidator:
    """Return the double validator installed on a delegate's editor.

    Args:
        delegate: The delegate under test.
        parent: Widget to parent the editor to.

    Returns:
        The editor's validator.
    """
    editor = _make_editor(delegate, parent)
    assert isinstance(editor, QtWidgets.QLineEdit)
    validator = editor.validator()
    assert isinstance(validator, QtGui.QDoubleValidator)
    return validator


class TestItemDelegate:
    """Tests for the composition-table percentage editor."""

    def test_create_editor_returns_a_line_edit(self, qtbot, parameters_page):
        """In-place percentage editing uses a QLineEdit."""
        delegate = ItemDelegate(parameters_page)

        assert isinstance(_make_editor(delegate, parameters_page), QtWidgets.QLineEdit)

    def test_editor_validator_is_a_double_validator(self, qtbot, parameters_page):
        """The editor rejects anything that is not a double."""
        editor = _make_editor(ItemDelegate(parameters_page), parameters_page)

        assert isinstance(editor, QtWidgets.QLineEdit)
        assert isinstance(editor.validator(), QtGui.QDoubleValidator)

    def test_editor_validator_spans_zero_to_one_hundred_percent(self, qtbot, parameters_page):
        """Atomic percentages are bounded to [0, 100] with 3 decimals."""
        validator = _make_validator(ItemDelegate(parameters_page), parameters_page)

        assert validator.bottom() == pytest.approx(0.0)
        assert validator.top() == pytest.approx(100.0)
        assert validator.decimals() == 3

    @pytest.mark.parametrize("text,state", AMOUNT_VALIDATION_CASES, ids=[case[0] for case in AMOUNT_VALIDATION_CASES])
    def test_validator_classifies_input(self, qtbot, parameters_page, text, state):
        """Only in-range percentages with at most 3 decimals are committable."""
        validator = _make_validator(ItemDelegate(parameters_page), parameters_page)

        assert validator.validate(text, len(text))[0] == state

    def test_init_forces_the_c_locale(self, qtbot, parameters_page):
        """Decimal parsing uses '.' regardless of the user's system locale."""
        ItemDelegate(parameters_page)

        assert QtCore.QLocale().language() == QtCore.QLocale.Language.C

    def test_delegate_is_installed_on_the_composition_table(self, parameters_page):
        """ParametersPage wires the delegate onto its composition table."""
        assert isinstance(parameters_page.parametersPage.tableWidget.itemDelegate(), ItemDelegate)


class TestBatchAmountDelegate:
    """Tests for the converter-style amount editor.

    Note: this delegate is defined in app.py but never installed on any view.
    """

    def test_create_editor_returns_a_line_edit(self, qtbot, batch_page):
        """Batch amount editing uses a QLineEdit."""
        delegate = BatchAmountDelegate(batch_page)

        assert isinstance(_make_editor(delegate, batch_page), QtWidgets.QLineEdit)

    def test_editor_validator_spans_the_extended_positive_range(self, qtbot, batch_page):
        """Batch amounts are bounded to (0, 999999] with 4 decimals."""
        validator = _make_validator(BatchAmountDelegate(batch_page), batch_page)

        assert validator.bottom() == pytest.approx(0.0001)
        assert validator.top() == pytest.approx(999999.0)
        assert validator.decimals() == 4

    @pytest.mark.parametrize("text,state", BATCH_VALIDATION_CASES, ids=[case[0] for case in BATCH_VALIDATION_CASES])
    def test_validator_classifies_input(self, qtbot, batch_page, text, state):
        """Only positive amounts up to 999999 are committable; 0 is not."""
        validator = _make_validator(BatchAmountDelegate(batch_page), batch_page)

        assert validator.validate(text, len(text))[0] == state


class TestAlignDelegate:
    """Tests for the centering delegate.

    Note: this delegate is defined in app.py but never installed on any view.
    """

    def test_init_style_option_centers_the_cell_text(self, qtbot, parameters_page):
        """Cells painted through this delegate are center-aligned."""
        delegate = AlignDelegate(parameters_page)
        option = QtWidgets.QStyleOptionViewItem()

        delegate.initStyleOption(option, QtCore.QModelIndex())

        assert option.displayAlignment == QtCore.Qt.AlignmentFlag.AlignCenter


class TestConfigureResultsTreeHeader:
    """Tests for the shared results-tree header sizing helper."""

    def test_last_section_does_not_stretch(self, qtbot, parameters_page):
        """Result columns keep their content width instead of stretching the last one."""
        assert not parameters_page.parametersPage.resultsTreeWidget.header().stretchLastSection()

    @pytest.mark.parametrize("page_attr,tree_attr", [("parameters_page", "parametersPage"), ("batch_page", "ui")])
    def test_only_column_seven_is_interactive(self, request, page_attr, tree_attr):
        """Every column auto-sizes to its contents except the one made resizable."""
        page = request.getfixturevalue(page_attr)
        tree = getattr(page, tree_attr).resultsTreeWidget
        header = tree.header()

        modes = [header.sectionResizeMode(column) for column in range(tree.columnCount())]
        expected = QtWidgets.QHeaderView.ResizeMode.ResizeToContents

        assert modes[INTERACTIVE_COLUMN] == QtWidgets.QHeaderView.ResizeMode.Interactive
        assert all(mode == expected for index, mode in enumerate(modes) if index != INTERACTIVE_COLUMN)

    def test_interactive_column_uses_the_default_section_width(self, qtbot, parameters_page):
        """The resizable column starts at the header's default width."""
        header = parameters_page.parametersPage.resultsTreeWidget.header()

        assert header.sectionSize(INTERACTIVE_COLUMN) == header.defaultSectionSize()

    def test_both_pages_start_with_identical_column_widths(self, qtbot, parameters_page, batch_page):
        """The two result trees are configured consistently."""
        parameters_tree = parameters_page.parametersPage.resultsTreeWidget
        batch_tree = batch_page.ui.resultsTreeWidget

        parameters_sizes = [parameters_tree.header().sectionSize(index) for index in range(parameters_tree.columnCount())]
        batch_sizes = [batch_tree.header().sectionSize(index) for index in range(batch_tree.columnCount())]

        assert parameters_sizes == batch_sizes

    def test_helper_is_idempotent(self, qtbot, parameters_page):
        """Re-applying the configuration does not change the resulting sizes."""
        tree = parameters_page.parametersPage.resultsTreeWidget
        before = [tree.header().sectionSize(index) for index in range(tree.columnCount())]

        configure_results_tree_header(tree)

        assert [tree.header().sectionSize(index) for index in range(tree.columnCount())] == before
