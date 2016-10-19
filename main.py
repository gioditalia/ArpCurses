#!/usr/bin/python

"""
    ArpCurses v1.0 - The ArpPoisoning tool.
    Copyright (C) 2016  Giovanni D'Italia

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import arpCurses


if __name__ == "__main__":
    if os.getuid() == 0:
        arpCurses.ArpCurses()
    else:
        print("\n\nI need ROOT permissions.\
            Sorry.\n\nPlease type: sudo "+sys.argv[0]+"\n\n")
