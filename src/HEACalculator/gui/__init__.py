"""GUI package for HEACalculator.

Imports the compiled Qt resource module so that embedded icons and images are
registered with the Qt resource system before any widget is constructed.
"""

from . import HEACalculator_rc  # noqa: F401 — registers Qt resources (icons/images)
