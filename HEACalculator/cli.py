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

from itertools import combinations_with_replacement, permutations

import numpy as np
import pandas as pd
import typer

from HEACalculator import HEACalculator
from HEACalculator.core.helpers import nested_formula_parser

app = typer.Typer()

@app.command(name='csv')
def csv_search(csv_file: str = typer.Argument(...)):
    """Calculates HEA parameters from the composition column of the given CSV file"""

    HEADER = ['Formula',
              'Density',
              'Delta',
              'Omega',
              'VEC',
              'Mixing Enthalpy',
              'Mixing Entropy',
              'Melting Temperature',]

    print(', '.join(HEADER))
    df = pd.read_csv(csv_file, usecols = lambda x : x.lower() in ['composition'])
    for alloy in df['composition']:
        print(', '.join(HEACalculator(alloy, csv=True).get_csv_list()))

@app.command(no_args_is_help=True, name='single')
def single_search(alloy: str = typer.Argument(...)):
    """Calculates HEA parameters of the given alloy"""
    try:
        print(HEACalculator(alloy))
    except Exception as e:
        raise typer.BadParameter(e)


@app.command(name='range')
def range_search(elements: str = typer.Option(...,
                                           help='List elements to search'),
                 start: float = typer.Option(0, min=0, max=100,
                                             help='Lowest composition for each element'),
                 end: float = typer.Option(100, min=0, max=100,
                                           help='Highest composition for each element'),
                 step: float = typer.Option(5, min=0,
                                            help='Composition screening step for each element'),
                 csv: bool = typer.Option(False, '--csv',
                                          help='Export results to stdout as a CSV file')):
    """Screens given composition range of the given elements"""
    if start > end:
        raise typer.BadParameter('The End option should be higher than the Start option')

    if csv:
        HEADER = ['Formula',
                  'Density',
                  'Delta',
                  'Omega',
                  'VEC',
                  'Mixing Enthalpy',
                  'Mixing Entropy',
                  'Formation Enthalpy',
                  'Melting Temperature',
                  'Crystal Structure',
                  'Model 1',
                  'Model 2',
                  'Model 3',
                  'Model 4',
                  'Model 5',
                  'Model 6',
                  'Model 7',
                  'Model 8', ]
        print(', '.join(HEADER))

    formula, composition_set = find_all_comps(elements, start, end, step)
    for composition in composition_set:
        new_alloy = ''.join(f'{k}{v}' for k, v in {**formula, **dict(zip(formula.keys(), composition))}.items())
        if csv:
            print(', '.join(HEACalculator(new_alloy).get_list()))
        else:
            print(HEACalculator(new_alloy))


def find_all_comps(alloy: str,
                   start: int,
                   end: int,
                   step: int):
    """Finds all composition possibilities"""

    formula = nested_formula_parser(alloy)
    no_of_elements = len(formula)
    composition_set = set()
    results = [i for i in combinations_with_replacement(np.arange(start, end, step), no_of_elements)
               if sum(i) == 100 if min(i) != 0]

    for result in results:
        for composition in permutations(result):
            composition_set.add(composition)

    return formula, composition_set
