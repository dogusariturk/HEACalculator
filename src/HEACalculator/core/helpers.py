"""Chemical formula parsing utilities."""

import math
import re

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

formula_token_matcher_rational = re.compile(r"[A-Z][a-z]?|(?:\d*[.])?\d+|\d+|[()]")


def _combine_level(units: list[tuple[dict[str, int | float], int | float]]) -> dict[str, int | float]:
    """Combine the ``(counts, count)`` units of one bracket level into element counts.

    When the counts add up to 100 or 1 they are shares: each unit is first scaled to
    one, so a group's count is its share of the level. Otherwise a count multiplies.

    Returns:
        Element counts for the level.

    Raises:
        ValueError: If a group given a share of the level has no nonzero count.
    """
    total = sum(count for _, count in units)
    shares = math.isclose(total, 100) or math.isclose(total, 1)
    combined: dict[str, int | float] = {}
    for counts, count in units:
        size = sum(counts.values())
        if shares and not size:
            raise ValueError("Input may not be a formula; a bracketed group has no nonzero count")
        scale = count / size if shares and size != 1 else count
        for ele, n in counts.items():
            combined[ele] = combined.get(ele, 0) + n * scale
    return combined


def nested_formula_parser(formula: str, check: bool = True) -> dict[str, int | float]:
    """Parse a chemical formula string into a dict of element counts.

    Handles nested round or square brackets, rational element counts and repeated
    chemical units, and drops elements with a zero count. An element or group
    without a count counts as 1. A count after a bracketed group multiplies every
    element in it, so ``(FeCo)2CrNi`` is Fe2Co2CrNi. The exception is a bracket level
    whose counts add up to 100 or 1, which reads as at.% or atomic fractions: there a
    group's count is its share of the level, split in the proportions written inside
    the group, so ``(CoCrFeNi)90Al10`` and ``Al10(CoCrFeNi)90`` are 10 at.% Al.
    Performs no sanity checking that elements are actually elements. Adapted from
    the Chemicals library.

    Args:
        formula (str): Formula string, simple formats only.
        check (bool): If ``True``, a simple check will be performed to determine
            if the input is a valid formula, and an exception will be raised if
            it is not. Defaults to True.

    Returns:
        Dictionary of counts of individual atoms, indexed by symbol with
            proper capitalization.

    Raises:
        ValueError: If brackets are unbalanced, a count has no element or bracket
            before it, a group given a share has no nonzero count, no element has a
            nonzero count, or (with ``check``) the formula contains anything besides
            symbols, counts, brackets and spaces.

    References:
        - Bell, C.; Cortes-Pena, Y.R.; and Contributors. Chemicals: Chemical Engineering Design Library (ChEDL).
        2016-2021. [https://github.com/CalebBell/chemicals](https://github.com/CalebBell/chemicals).
    """
    formula = formula.replace("[", "(").replace("]", ")")

    tokens = formula_token_matcher_rational.findall(formula)
    if check and "".join(tokens) != "".join(formula.split()):
        raise ValueError("Input may not be a formula; unrecognized characters were detected")

    stack: list[list[tuple[dict[str, int | float], int | float]]] = [[]]
    for token in tokens:
        if token == "(":
            stack.append([])
        elif token == ")":
            if len(stack) == 1:
                raise ValueError("Input may not be a formula; unbalanced brackets")
            group = _combine_level(stack.pop())
            stack[-1].append((group, 1))
        elif token.isalpha():
            stack[-1].append(({token: 1}, 1))
        else:
            if not stack[-1]:
                raise ValueError("Input may not be a formula; a count must follow an element or bracket")
            v = float(token)
            counts, count = stack[-1][-1]
            stack[-1][-1] = (counts, count * (int(v) if v.is_integer() else v))
    if len(stack) > 1:
        raise ValueError("Input may not be a formula; unbalanced brackets")
    ans = {ele: count for ele, count in _combine_level(stack[0]).items() if count}
    if not ans:
        raise ValueError("Input may not be a formula; no element has a nonzero count")
    return ans
