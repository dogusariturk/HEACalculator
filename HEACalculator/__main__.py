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

import typer

from HEACalculator.cli import app as cli_app
from HEACalculator.gui import app as gui_app

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(gui_app,
              name='gui',
              help='Starts the HEACalculator Graphical User Interface (GUI)')
app.add_typer(cli_app,
              name='search',
              help='Parameter search commands',
              no_args_is_help=True)


@app.callback(no_args_is_help=True,
              context_settings={'help_option_names': ["-h", "--help"]})
def main():
    """A tool for calculating High-Entropy Alloy (HEA) specific parameters and solid-solution predictions"""


if __name__ == '__main__':
    app()
