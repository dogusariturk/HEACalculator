"""Chemical formula parsing utilities."""

import re

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

formula_token_matcher_rational = re.compile(r"[A-Z][a-z]?|(?:\d*[.])?\d+|\d+|[()]")


def nested_formula_parser(formula: str, check: bool = True) -> dict[str, int | float]:
    """Parse a chemical formula string into a dict of element counts.

    Handles nested round or square brackets and their multipliers, as well as
    rational element counts. Accepts repeated chemical units and drops elements
    with a zero count. Performs no sanity checking that elements are actually
    elements. Implemented from the Chemicals library.

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
            before it, no element has a nonzero count, or (with ``check``) the
            formula contains anything besides symbols, counts, brackets and spaces.

    References:
        - Bell, C.; Cortes-Pena, Y.R.; and Contributors. Chemicals: Chemical Engineering Design Library (ChEDL).
        2016-2021. [https://github.com/CalebBell/chemicals](https://github.com/CalebBell/chemicals).
    """
    formula = formula.replace("[", "(").replace("]", ")")

    stack = [[]]
    last = stack[0]
    tokens = formula_token_matcher_rational.findall(formula)
    if check and "".join(tokens) != "".join(formula.split()):
        raise ValueError("Input may not be a formula; unrecognized characters were detected")

    for token in tokens:
        if token == "(":
            stack.append([])
            last = stack[-1]
        elif token == ")":
            if len(stack) == 1:
                raise ValueError("Input may not be a formula; unbalanced brackets")
            temp_dict = {}
            for d in last:
                for ele, count in d.items():
                    if ele in temp_dict:
                        temp_dict[ele] = temp_dict[ele] + count
                    else:
                        temp_dict[ele] = count
            stack.pop()
            last = stack[-1]
            last.append(temp_dict)
        elif token.isalpha():
            last.append({token: 1})
        else:
            if not last:
                raise ValueError("Input may not be a formula; a count must follow an element or bracket")
            v = float(token)
            v_int = int(v)
            if v_int == v:
                v = v_int
            last[-1] = {ele: count * v for ele, count in last[-1].items()}
    if len(stack) > 1:
        raise ValueError("Input may not be a formula; unbalanced brackets")
    ans = {}
    for d in last:
        for ele, count in d.items():
            if ele in ans:
                ans[ele] = ans[ele] + count
            else:
                ans[ele] = count
    ans = {ele: count for ele, count in ans.items() if count}
    if not ans:
        raise ValueError("Input may not be a formula; no element has a nonzero count")
    return ans
