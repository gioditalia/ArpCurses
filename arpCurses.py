# -*- coding: utf-8 -*-
import poison
import tools
import curses
import time
import sys
import arpAttack
import arpScan
import curses.textpad
from scapy.route import *

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
        self.length_win = 85
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
        victim = makeTextBox(self.base_Y,self.base_X,16)
        router = makeTextBox(self.base_Y,self.base_X+23,16)

        #select interface for this session
        interface = self.__drawSelectInterface() #not use self.interface for consistency with victim_ip and router_ip?
        
        self.stdscr.clear()
        
        #init attack module
        attack = arpAttack.ArpAttack(self.stdscr,interface)
        scan = arpScan.ArpScan(stdscr,interface)
        
        #future features
        #sniff = arpSniff.ArpSniff(stdscr)
        
        digit = "1"
        while 1:
            if digit == "1":
                digit,victim_ip,router_ip = attack.main(victim,router)
            elif digit == "2":
                digit,victim_ip,router_ip = scan.main(victim,router)
            #if digit == "3":
                #sniff
            elif digit == "4":
                stdscr.clear()
                self.__drawNetworkTab()
                digit = self.stdscr.getkey()
            elif digit == "q":
                tools.firewallBlockingConf(interface)
                sys.exit(1)
            else:
                digit = self.stdscr.getkey()
                
    def __drawSelectInterface(self):
        iface = makeTextBox(7,20,10)
        while 1:
            self.stdscr.addstr(0, 0, (" "*self.length_win),curses.color_pair(2))
            self.stdscr.addstr(0, 0, "Please set your network interface",curses.color_pair(2))
            drawTitle(self.stdscr,1,10)
            drawBox(self.stdscr,7,20,20,"","iFace")    
            try:
                interface = iface.edit().split(" ")[0]
                tools.firewallBlockingConf(interface)
                break
            except:
                infoBox(self.stdscr,6,15,
                    " Error to set interface ","Error!")
            self.stdscr.clear()
        return interface
            
        
    def __drawNetworkTab(self):
        curses.textpad.rectangle(self.stdscr, self.base_Y,self.base_X-1, self.base_Y+16, self.base_X+81)
        self.stdscr.addstr(self.base_Y,self.base_X+1,"Network Monitor",curses.color_pair(1))
        y = 4
        for i in str(conf.route).split("\n"):
            self.stdscr.addstr(y,3,i,curses.color_pair(1))
            y+=1
        #draw tabs navigator        
        self.stdscr.addstr(0, 0, (" "*self.length_win),curses.color_pair(2))
        self.stdscr.addstr(0, 0, "1.Attack    2.Scan    3.Sniff    4.Network    Q.Quit",curses.color_pair(2))
        self.stdscr.addstr(0, 33, "4.Network",curses.color_pair(3))
            
def drawTitle(stdscr,y,x):
    #draw title
    stdscr.addstr(y, x, "    _             ___        ",curses.color_pair(1))
    stdscr.addstr(y+1, x, "   /_\  _ _ _ __ / __|  _ _ _ ___ ___ ___",curses.color_pair(1))
    stdscr.addstr(y+2, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
            
def drawBox(stdscr,y,x,length=1,text="",label=""):
    if length == 0:
        length = len(text)
    curses.textpad.rectangle(stdscr, y,x, 1+y+1, length+x)
    stdscr.addstr(y+1, x+1, text,curses.color_pair(1))
    if label != "":
        stdscr.addstr(y, x+1, label,curses.color_pair(1))
    stdscr.refresh()
    return x+1,y+1
    
def makeTextBox(y,x,length=1):
    win = curses.newwin(1, length, y+1, x+1) #y+1 and x+1 for fit perfect whit drawBox
    win.bkgd(' ',curses.color_pair(1))
    return curses.textpad.Textbox(win)

def infoBox(stdscr,y,x,msg,title="infobox"):
    curses.textpad.rectangle(stdscr, y,x, y+4, len(msg)+x+1)    #draw message box
    stdscr.addstr(y, x+1, title,curses.color_pair(1)) #set box title
    stdscr.addstr(y+1, x+1, (" "*(len(msg))),curses.color_pair(1)) #set color all box
    stdscr.addstr(y+2, x+1, (" "*(len(msg))),curses.color_pair(1))
    stdscr.addstr(y+3, x+1, (" "*(len(msg))),curses.color_pair(1))
    stdscr.addstr(y+1, x+1, msg,curses.color_pair(1))   #write message
    stdscr.addstr(y+3, (x*2+len(msg))/2, "Ok",curses.color_pair(1))   #write ok
    stdscr.getkey() #wait any key

if __name__ == "__main__":
       Main()
