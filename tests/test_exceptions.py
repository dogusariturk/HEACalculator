"""Tests for the custom exception classes defined in HEACalculator.exceptions."""

import pytest

from HEACalculator.exceptions import (
    ElementNotFoundError,
    MissingFormationEnthalpyError,
    MissingMixingEnthalpyError,
    MissingPairDataError,
)


class TestExceptionHierarchy:
    """Tests for exception inheritance relationships."""

    def test_missing_mixing_enthalpy_error_is_missing_pair_data_error(self):
        """MissingMixingEnthalpyError is a subclass of MissingPairDataError."""
        assert issubclass(MissingMixingEnthalpyError, MissingPairDataError)

    def test_missing_formation_enthalpy_error_is_missing_pair_data_error(self):
        """MissingFormationEnthalpyError is a subclass of MissingPairDataError."""
        assert issubclass(MissingFormationEnthalpyError, MissingPairDataError)

    def test_missing_pair_data_error_is_key_error(self):
        """MissingPairDataError is a subclass of KeyError."""
        assert issubclass(MissingPairDataError, KeyError)

    def test_element_not_found_error_is_key_error(self):
        """ElementNotFoundError is a subclass of KeyError."""
        assert issubclass(ElementNotFoundError, KeyError)

    def test_missing_mixing_enthalpy_error_is_key_error(self):
        """MissingMixingEnthalpyError is catchable as a KeyError (transitive)."""
        assert issubclass(MissingMixingEnthalpyError, KeyError)

    def test_missing_formation_enthalpy_error_is_key_error(self):
        """MissingFormationEnthalpyError is catchable as a KeyError (transitive)."""
        assert issubclass(MissingFormationEnthalpyError, KeyError)


class TestExceptionInstantiation:
    """Tests for direct instantiation and raising of custom exceptions."""

    def test_missing_mixing_enthalpy_error_can_be_raised_and_caught_as_key_error(self):
        """MissingMixingEnthalpyError raised by data layer is catchable as KeyError."""
        with pytest.raises(KeyError):
            raise MissingMixingEnthalpyError(("Fe", "Xx"))

    def test_missing_formation_enthalpy_error_can_be_raised_and_caught_as_key_error(self):
        """MissingFormationEnthalpyError raised by data layer is catchable as KeyError."""
        with pytest.raises(KeyError):
            raise MissingFormationEnthalpyError(("Fe", "Xx"))

    def test_element_not_found_error_can_be_raised_and_caught_as_key_error(self):
        """ElementNotFoundError raised by data layer is catchable as KeyError."""
        with pytest.raises(KeyError):
            raise ElementNotFoundError("Xx")

    def test_missing_mixing_enthalpy_error_stores_key(self):
        """MissingMixingEnthalpyError stores the pair key as its first argument."""
        key = ("Fe", "Xx")
        exc = MissingMixingEnthalpyError(key)
        assert exc.args[0] == key

    def test_missing_formation_enthalpy_error_stores_key(self):
        """MissingFormationEnthalpyError stores the pair key as its first argument."""
        key = ("Fe", "Xx")
        exc = MissingFormationEnthalpyError(key)
        assert exc.args[0] == key

    def test_element_not_found_error_stores_symbol(self):
        """ElementNotFoundError stores the element symbol as its first argument."""
        exc = ElementNotFoundError("Xx")
        assert exc.args[0] == "Xx"

    def test_missing_mixing_enthalpy_error_caught_as_missing_pair_data_error(self):
        """MissingMixingEnthalpyError is catchable as MissingPairDataError."""
        with pytest.raises(MissingPairDataError):
            raise MissingMixingEnthalpyError(("Fe", "Xx"))

    def test_missing_formation_enthalpy_error_caught_as_missing_pair_data_error(self):
        """MissingFormationEnthalpyError is catchable as MissingPairDataError."""
        with pytest.raises(MissingPairDataError):
            raise MissingFormationEnthalpyError(("Fe", "Xx"))
