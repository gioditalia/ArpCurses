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

import poison
import tools
import curses
import time
import sys
import arpAttack
import arpScan
import arpNetwork
import arpSniff
import utils
import curses.textpad
from scapy.route import *


class ArpCurses():

    def __init__(self):
        """
        Set global variables ,colors and
        """
        self.base_X = 1
        self.base_Y = 2
        self.length_win = 80
        #copyright string
        self.GPLv3 = "ArpCurses Copyright (C) 2016  Giovanni D'Italia\n"\
        +"This program comes with ABSOLUTELY NO WARRANTY.\n"\
        +"This is free software, and you are welcome to redistribute it,\n"\
        +"under certain conditions."
        #set colors
        curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
        curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
        #launch curses.wrapper
        curses.wrapper(self.main)

    def main(self,stdscr):
        """
        launch the curses's tabs
        """
        self.stdscr = stdscr
        
        # Clear screen
        self.stdscr.clear()
        
        #set background
        self.stdscr.bkgd('\t',curses.color_pair(1))

        #victim e router text box
        victim = utils.makeTextBox(self.base_Y,self.base_X,16)
        router = utils.makeTextBox(self.base_Y,self.base_X+23,16)

        #select interface for this session
        interface = self.__drawSelectInterface()
        
        self.stdscr.clear()
        
        #initialize modules
        attack = arpAttack.ArpAttack(self.stdscr,interface)
        scan = arpScan.ArpScan(self.stdscr,interface)
        network = arpNetwork.ArpNetwork(self.stdscr,interface)
        
        #future features
        sniff = arpSniff.ArpSniff(self.stdscr,interface)
        
        self.__drawTabContent()
        digit = self.stdscr.getkey()
        
        while 1:
            if digit == "1":
                digit = attack.main(victim,router)
            elif digit == "2":
                digit = scan.main(victim,router)
            elif digit == "3":
                digit = sniff.main(victim,router)
            elif digit == "4":
                stdscr.clear()
                digit = network.main(victim,router)
            elif digit == "q":
                if utils.quitBox(self.stdscr,6,15,
                    "Do you really want to quit?",""):
                    tools.firewallBlockingConf(interface)
                    sys.exit(1)
                else:
                    self.__drawTabContent()
                    digit = self.stdscr.getkey()
            else:
                digit = self.stdscr.getkey()
                
    def __drawSelectInterface(self):
        iface = utils.makeTextBox(7,20,10)
        interface = ""
        while 1:
            self.stdscr.addstr(0, 0, (" "*self.length_win),
                curses.color_pair(2))
            self.stdscr.addstr(0, 0, "Please set your network interface",
                curses.color_pair(2))
            utils.drawTitle(self.stdscr,1,10)
            utils.drawBox(self.stdscr,7,20,20,interface,"iFace")
            try:
                interface = iface.edit().strip()
                if interface == conf.iface:
                    tools.firewallBlockingConf(interface)
                    break
                else:
                    utils.infoBox(self.stdscr,6,15,
                        " Interface not found ","Error!")
            except:
                utils.infoBox(self.stdscr,6,15,
                    " Error to set interface ","Error!")
            self.stdscr.clear()
        return interface
    
    def __drawTabContent(self):
        self.stdscr.clear()
        utils.drawMenuBar(self.stdscr,self.length_win)
        utils.drawTitle(self.stdscr,1,10)
        self.stdscr.addstr(8, 0, self.GPLv3,curses.color_pair(1))
        self.stdscr.refresh()

if __name__ == "__main__":
       ArpCurses()
