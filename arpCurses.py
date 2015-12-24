# -*- coding: utf-8 -*-
import poison
import tools
import curses
import time
import sys
import arpAttack
import curses.textpad

class Main():

    def __init__(self):
        print "execute in curses mode..."
        for i in range(0,2):
            time.sleep(1)
        self.interface = ""
        curses.wrapper(self.main)

    def main(self,stdscr):
        """
        Set global variables ,colors and launch 
        the curses's tabs(in 1.0 version only arpAttack())
        """
        
        self.stdscr = stdscr
        
        # Clear screen
        self.stdscr.clear()
        
        #set colors
        curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
        curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
        
        #set background
        self.stdscr.bkgd('\t',curses.color_pair(1))

        #select interface for this session
        self.drawSelectInterface()
        self.stdscr.clear()
        
        #init attack module
        attack = arpAttack.ArpAttack(self.stdscr,self.interface)
        
        #future features
        #scan = arpScan.ArpScan(stdscr)
        #sniff = arpSniff.ArpSniff(stdscr)
        
        digit = "1"
        while 1:
            if digit == "1":
                digit = attack.main()
            #if digit == "2":
                #scan
            #if digit == "3":
                #sniff
            elif digit == "q":
                tools.firewallBlockingConf(self.interface)
                sys.exit(1)
            else:
                stdscr.clear()
                self.drawExitTab()
                digit = self.stdscr.getkey()
                
    def drawSelectInterface(self):
        interface = makeTextBox(7,20,16)
        while 1:
            self.stdscr.addstr(0, 0, (" "*60),curses.color_pair(2))
            self.stdscr.addstr(0, 0, "Please set your network interface",curses.color_pair(2))
            drawTitle(self.stdscr,1,10)
            drawBox(self.stdscr,7,20,20,"","iFace")    
            try:
                self.interface = interface.edit().split(" ")[0]
                tools.firewallBlockingConf(self.interface)
                break
            except:
                infoBox(self.stdscr,6,15,
                    " Error to set interface ","Error!")
            self.stdscr.clear()
            
    def drawExitTab(self):
        drawTitle(self.stdscr,1,10)
        #exit tab content
        self.stdscr.addstr(10,0,"press one more time Q to exit.",curses.color_pair(1))
        #draw tabs navigator        
        self.stdscr.addstr(0, 0, (" "*60),curses.color_pair(2))
        self.stdscr.addstr(0, 0, "1.Attack    2.Scan    3.Sniff    Q.Quit",curses.color_pair(2))
        self.stdscr.addstr(0, 33, "Q.Quit",curses.color_pair(3))
            
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
