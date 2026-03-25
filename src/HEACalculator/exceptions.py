"""Package-level exceptions for HEACalculator."""

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"


class MissingPairDataError(KeyError):
    """Raised when a binary element pair has no entry in a data database."""


class MissingMixingEnthalpyError(MissingPairDataError):
    """Raised when a binary element pair has no mixing enthalpy entry."""


class MissingFormationEnthalpyError(MissingPairDataError):
    """Raised when a binary element pair has no formation enthalpy entry."""


class ElementNotFoundError(KeyError):
    """Raised when an element symbol has no entry in the element database."""
