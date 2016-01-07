#!/usr/bin/python
import arpCurses
import os
import sys

if __name__ == "__main__":
    if os.getuid() == 0:
       arpCurses.Main()
    else:
       print("\n\nI need ROOT permissions.\
        Sorry.\n\nPlease type: sudo "+sys.argv[0]+"\n\n")
