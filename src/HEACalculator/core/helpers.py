"""Chemical formula parsing utilities."""

import re
import string

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

formula_token_matcher_rational = re.compile(r"[A-Z][a-z]?|(?:\d*[.])?\d+|\d+|[()]")
letter_set = set(string.ascii_letters)
bracketed_charge_re = re.compile(r"\([+-]?\d+\)$|\(\d+[+-]?\)$|\([+-]+\)$")


def nested_formula_parser(formula: str, check: bool = True) -> dict[str, int | float]:
    """Parse a chemical formula string into a dict of element counts.

    Handles nested brackets and their multipliers, as well as rational element
    counts. Strips charges from the end of a formula first. Accepts repeated
    chemical units. Performs no sanity checking that elements are actually
    elements. Implemented from the Chemicals library.

    Args:
        formula (str): Formula string, simple formats only.
        check (bool): If ``True``, a simple check will be performed to determine
            if the input is a valid formula, and an exception will be raised if
            it is not. Defaults to True.

    Returns:
        dict: Dictionary of counts of individual atoms, indexed by symbol with
            proper capitalization.

    References:
        Bell, C.; Cortes-Pena, Y.R.; and Contributors. Chemicals: Chemical Engineering Design Library (ChEDL).
        2016-2021. https://github.com/CalebBell/chemicals.
    """
    formula = formula.replace("[", "").replace("]", "")
    charge_splits = bracketed_charge_re.split(formula)
    formula = charge_splits[0] if len(charge_splits) > 1 else formula.split("+")[0].split("-")[0]

    stack = [[]]
    last = stack[0]
    tokens = formula_token_matcher_rational.findall(formula)
    if check:
        token_letters = {j for i in tokens for j in i if j in letter_set}
        formula_letters = {i for i in formula if i in letter_set}
        if formula_letters != token_letters:
            raise ValueError("Input may not be a formula; extra letters were detected")

    for token in tokens:
        if token == "(":
            stack.append([])
            last = stack[-1]
        elif token == ")":
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
            v = float(token)
            v_int = int(v)
            if v_int == v:
                v = v_int
            last[-1] = {ele: count * v for ele, count in last[-1].items()}
    ans = {}
    for d in last:
        for ele, count in d.items():
            if ele in ans:
                ans[ele] = ans[ele] + count
            else:
                ans[ele] = count
    return ans
