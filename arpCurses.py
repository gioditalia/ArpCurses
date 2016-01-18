# -*- coding: utf-8 -*-
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


class Main():

    def __init__(self):
        print "execute in curses mode..."
        for i in range(0,2):
            time.sleep(1)
        curses.wrapper(self.main)

    def main(self,stdscr):
        """
        Set global variables ,colors and launch 
        the curses's tabs
        """
        self.base_X = 1
        self.base_Y = 2
        self.length_win = 80
        self.stdscr = stdscr
        
        # Clear screen
        self.stdscr.clear()
        
        #set colors
        curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
        curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
        
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
        
        utils.drawMenuBar(self.stdscr,self.length_win)
        utils.drawTitle(self.stdscr,1,10)
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
                tools.firewallBlockingConf(interface)
                if utils.quitBox(self.stdscr,6,15,
                    "Do you really want to quit?",""):
                    sys.exit(1)
                else:
                    self.stdscr.clear()
                    utils.drawMenuBar(self.stdscr,self.length_win)
                    utils.drawTitle(self.stdscr,1,10)
                    digit = self.stdscr.getkey()
            else:
                digit = self.stdscr.getkey()
                
    def __drawSelectInterface(self):
        iface = utils.makeTextBox(7,20,10)
        while 1:
            self.stdscr.addstr(0, 0, (" "*self.length_win),
                curses.color_pair(2))
            self.stdscr.addstr(0, 0, "Please set your network interface",
                curses.color_pair(2))
            utils.drawTitle(self.stdscr,1,10)
            utils.drawBox(self.stdscr,7,20,20,"","iFace")    
            try:
                interface = iface.edit().split(" ")[0]
                tools.firewallBlockingConf(interface)
                break
            except:
                utils.infoBox(self.stdscr,6,15,
                    " Error to set interface ","Error!")
            self.stdscr.clear()
        return interface

if __name__ == "__main__":
       Main()
