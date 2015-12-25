import tools
import curses
import sys
import arpCurses
import curses.textpad


class ArpScan():

    def __init__(self,stdscr,interface):
    
        self.base_X = 1
        self.base_Y = 2
        self.length_win = 85
        self.stdscr = stdscr
        
        self.interface = interface #physical interface
        
        self.network = arpCurses.makeTextBox(self.base_Y+4,self.base_X,16)
        
        self.network_CIDR = "192.168.0.0/24"
        self.res = [["","",""]]
        
        

        
    def main(self,victim,router):
    
        self.victim_ip = victim.gather().split(" ")[0] #victim address
        self.router_ip = router.gather().split(" ")[0] #router address

        while 1:
            self.__drawTabContent()
            
            #wait key's pression
            digit = self.stdscr.getkey()
            
            #arpcurses generic menu
            if digit == "1" or digit == "3" or digit == "4" or digit == "q":
                return digit,self.victim_ip,self.router_ip
            
            if digit == "v":    #set victim ip
                try:
                    self.victim_ip = victim.edit().split(" ")[0]
                except:
                    arpCurses.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid victim IP ","Error!")
                    self.victim_ip = ""

            if digit == "r":    #set router ip
                try:
                    self.router_ip = router.edit().split(" ")[0]
                except:
                    arpCurses.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid router IP ","Error!")
                    self.router_ip = ""
            
            if digit == "n":    #set router ip
                try:
                    self.network_CIDR = self.network.edit().split(" ")[0]
                except:
                    arpCurses.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid router IP ","Error!")
                    self.network_CIDR = ""
            
            if digit == "s":
                #try:
                    self.res = tools.scan(self.network_CIDR,self.interface)
                    
                #except:
                #    arpCurses.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                #            " Something going wrong, control your settings ","Error!")
            
            
            
    def __drawTabContent(self):
        #clear screen
        self.stdscr.clear()
        
        #draw textbox with label
        arpCurses.drawBox(self.stdscr,self.base_Y,self.base_X,20,self.victim_ip,"Victim")
        self.stdscr.addstr(self.base_Y,self.base_X+1,"V",curses.color_pair(2))
    
        arpCurses.drawBox(self.stdscr,self.base_Y,self.base_X+23,20,self.router_ip,"Router")
        self.stdscr.addstr(self.base_Y, self.base_X+24, "R",curses.color_pair(2))
        
        arpCurses.drawBox(self.stdscr,self.base_Y+4,self.base_X,20,self.network_CIDR,"Network(CIDR)")
        self.stdscr.addstr(self.base_Y+4, self.base_X+1, "N",curses.color_pair(2))
                
        arpCurses.drawBox(self.stdscr,self.base_Y+4,self.base_X+23,20,self.interface,"iFace")
        
        curses.textpad.rectangle(self.stdscr, self.base_Y+7,self.base_X, self.base_Y+16, self.base_X+70)
        self.stdscr.addstr(self.base_Y+7,self.base_X+1,"Scan",curses.color_pair(1))
        self.stdscr.addstr(self.base_Y+7, self.base_X+1, "S",curses.color_pair(2))
        self.stdscr.addstr(self.base_Y+8,self.base_X+1," Mac Address               Ip Address       Hostname",curses.color_pair(1))
        y = self.base_Y+9
        for MAC,ip,host in self.res:
            self.stdscr.addstr(y,self.base_X+2,MAC,curses.color_pair(1))
            self.stdscr.addstr(y,self.base_X+28,ip,curses.color_pair(1))
            self.stdscr.addstr(y,self.base_X+45,host,curses.color_pair(1))
            y+=1
        
        #draw tabs navigator
        self.stdscr.addstr(0, 0, (" "*self.length_win),curses.color_pair(2))
        self.stdscr.addstr(0, 0, "1.Attack    2.Scan    3.Sniff    4.Network    Q.Quit",curses.color_pair(2))
        self.stdscr.addstr(0, 12, "2.Scan",curses.color_pair(3))
        self.stdscr.refresh()
