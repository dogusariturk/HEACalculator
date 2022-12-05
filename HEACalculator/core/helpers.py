#!/usr/bin/env python3

# Copyright (C) 2022  Doguhan Sariturk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import string

__author__ = "Doguhan Sariturk"
__email__ = "dogu.sariturk@gmail.com"

formula_token_matcher_rational = re.compile(r'[A-Z][a-z]?|(?:\d*[.])?\d+|\d+|[()]')
letter_set = set(string.ascii_letters)
bracketed_charge_re = re.compile(r'\([+-]?\d+\)$|\(\d+[+-]?\)$|\([+-]+\)$')


def nested_formula_parser(formula, check=True):
    """Improved formula parser which handles braces and their multipliers,
    as well as rational element counts.

    Implemented from Chemicals library. See below for the citation.

    Strips charges from the end of a formula first. Accepts repeated chemical
    units. Performs no sanity checking that elements are actually elements.
    As it uses regular expressions for matching, errors are mostly just ignored.

    References
    ----------
    Caleb Bell, Yoel Rene Cortes-Pena, and Contributors (2016-2021).
    Chemicals: Chemical properties component of Chemical Engineering Design Library (ChEDL)
    https://github.com/CalebBell/chemicals.

    Parameters
    ----------
    formula : str
        Formula string, very simply formats only.
    check : bool
        If `check` is True, a simple check will be performed to determine if
        a formula is not a formula and an exception will be raised if it is
        not, [-]

    Returns
    -------
    atoms : dict
        dictionary of counts of individual atoms, indexed by symbol with
        proper capitalization, [-]
    """
    formula = formula.replace('[', '').replace(']', '')
    charge_splits = bracketed_charge_re.split(formula)
    if len(charge_splits) > 1:
        formula = charge_splits[0]
    else:
        formula = formula.split('+')[0].split('-')[0]

    stack = [[]]
    last = stack[0]
    tokens = formula_token_matcher_rational.findall(formula)
    if check:
        token_letters = set([j for i in tokens for j in i if j in letter_set])
        formula_letters = set(i for i in formula if i in letter_set)
        if formula_letters != token_letters:
            raise Exception('Input may not be a formula; extra letters were detected')

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
