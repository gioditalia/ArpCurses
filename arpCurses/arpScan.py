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

import tools
import curses
import utils
import curses.textpad


class ArpScan():

    def __init__(self, stdscr, interface):

        self.base_X = 1
        self.base_Y = 2
        self.length_win = 80
        self.stdscr = stdscr

        self.interface = interface  # physical interface

        self.network = utils.makeTextBox(self.base_Y+4, self.base_X, 16)

        self.network_CIDR = ""
        self.res = [["", "", ""]]

    def main(self, victim, router):

        self.victim_ip = victim.gather().strip()  # victim address
        self.router_ip = router.gather().strip()  # router address

        while 1:
            self.__drawTabContent()

            # wait key's pression
            digit = self.stdscr.getkey()

            # arpcurses generic menu
            if utils.menuSelects(digit):
                return digit

            # victim/router ip set menu
            if digit == "v":    # set victim ip
                try:
                    self.victim_ip = victim.edit().strip()
                except:
                    utils.infoBox(self.stdscr, self.base_Y+1, self.base_X+10,
                                  " Invalid victim IP ", "Error!")
                    self.victim_ip = ""

            if digit == "r":    # set router ip
                try:
                    self.router_ip = router.edit().strip()
                except:
                    utils.infoBox(self.stdscr, self.base_Y+1, self.base_X+10,
                                  " Invalid router IP ", "Error!")
                    self.router_ip = ""

            # scanner menu
            if digit == "n":    # set router ip
                try:
                    self.network_CIDR = self.network.edit().strip()
                except:
                    utils.infoBox(self.stdscr, self.base_Y+1, self.base_X+10,
                                  " Invalid router IP ", "Error!")
                    self.network_CIDR = ""

            if digit == "s":
                if not self.network_CIDR == "":
                    try:
                        self.res = tools.scan(self.network_CIDR,
                                              self.interface)
                    except:
                        utils.infoBox(self.stdscr, self.base_Y+1,
                                      self.base_X+10, " Something going wrong,"
                                      " control your settings ",
                                      "Error!")

    def __drawTabContent(self):
        # clear screen
        self.stdscr.clear()

        # draw textbox with label
        utils.drawBox(self.stdscr, self.base_Y, self.base_X, 20,
                      self.victim_ip, "Victim")
        self.stdscr.addstr(self.base_Y, self.base_X+1, "V",
                           curses.color_pair(2))

        utils.drawBox(self.stdscr, self.base_Y, self.base_X+23, 20,
                      self.router_ip, "Router")
        self.stdscr.addstr(self.base_Y, self.base_X+24, "R",
                           curses.color_pair(2))

        utils.drawBox(self.stdscr, self.base_Y+4, self.base_X, 20,
                      self.network_CIDR, "Network(CIDR)")
        self.stdscr.addstr(self.base_Y+4, self.base_X+1, "N",
                           curses.color_pair(2))

        utils.drawBox(self.stdscr, self.base_Y+4, self.base_X+23, 20,
                      self.interface, "iFace")

        curses.textpad.rectangle(self.stdscr,
                                 self.base_Y+7, self.base_X,
                                 self.base_Y+16, self.base_X+70)
        self.stdscr.addstr(self.base_Y+7, self.base_X+1, "Scan",
                           curses.color_pair(1))
        self.stdscr.addstr(self.base_Y+7, self.base_X+1, "S",
                           curses.color_pair(2))
        self.stdscr.addstr(self.base_Y+8, self.base_X+1,
                           " Mac Address               Ip Address       "
                           "Hostname", curses.color_pair(1))

        y = self.base_Y+9
        for MAC, ip, host in self.res:
            self.stdscr.addstr(y, self.base_X+2, MAC, curses.color_pair(1))
            self.stdscr.addstr(y, self.base_X+28, ip, curses.color_pair(1))
            self.stdscr.addstr(y, self.base_X+45, host, curses.color_pair(1))
            y += 1

        # draw tabs navigator
        utils.drawMenuBar(self.stdscr, self.length_win)
        self.stdscr.addstr(0, 12, "2.Scan", curses.color_pair(3))
        self.stdscr.refresh()
