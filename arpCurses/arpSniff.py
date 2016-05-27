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

import curses
import utils
import datetime
import threading
import sys
from scapy.layers.l2 import *
from scapy.layers.inet import *

class ArpSniff():

    def __init__(self,stdscr,interface):
        
        self.base_X = 1
        self.base_Y = 2
        self.length_win = 80
        self.stdscr = stdscr
        
        self.sniff_status = False #sniff status
        self.interface = interface #physical interface
        self.pkt = [] #packets array
        
        self.savedir = utils.makeTextBox(self.base_Y,self.base_X+46,100)
        self.savingdir = "./"
        self.savingdir_show = self.savingdir
        self.filter = utils.makeTextBox(self.base_Y+3,self.base_X,70)
        self.filter_str = ""
        
    def main(self,victim,router):

        self.victim_ip = victim.gather().strip() #victim address
        self.router_ip = router.gather().strip() #router address
        self.tab_status = True #enable write sniff packets

        while 1:
            self.__drawTabContent()
            
            #wait key's pression
            digit = self.stdscr.getkey()
            
            #arpcurses generic menu
            if digit == "1" or digit == "2" or digit == "4" or digit == "q":
                self.tab_status = False #disable write sniff packets
                return digit
            
            if digit == "v":    #set victim ip
                try:
                    self.victim_ip = victim.edit().strip() #remove empty
                except:
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid victim IP ","Error!")
                    self.victim_ip = ""

            if digit == "r":    #set router ip
                try:
                    self.router_ip = router.edit().strip()
                except:
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                            " Invalid router IP ","Error!")
                    self.router_ip = ""
                    
            if digit == "s":    #start/stop sniff
                if self.victim_ip == "":
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+10,
                        " You must set victim IP ","Error!")
                else:
                    self.sniff_status = not self.sniff_status
                    if self.sniff_status:
                        try:
                            t = threading.Thread(target=self.__sniff)
                            t.setDaemon(True)
                            t.start()
                        except:
                            self.attack_status = False
                            utils.infoBox(self.stdscr,
                            self.base_Y+1,self.base_X+1,
                            " Something going wrong, control your settings ",
                            "Error!")
                    else:
                        if utils.saveBox(self.stdscr,6,15,
                            "Save sniffed packets in .cap file?",""):
                            self.__save()

            if digit == "d":
                self.__drawSaveDir()
                self.savingdir = self.savedir.edit().strip()
                if not self.savingdir[len(self.savingdir)-1] == "/":
                    self.savingdir= "%s/" %(self.savingdir)
                self.savingdir_show = self.savingdir
                if len(self.savingdir_show) > 32:
                    self.savingdir_show =".../%s" %(self.savingdir_show[-27:])
                    
            if digit == "f":
                if self.sniff_status:
                    utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+5,
                        " You must stop sniffig before change filter ","Error!")
                else:
                    self.filter_str = self.filter.edit()
                    for i in xrange(0,len(self.filter_str)-1):
                        if self.filter_str[i] == " " \
                        and self.filter_str[i+1] == " ":
                            self.filter_str = self.filter_str[:i-1]
                    
    def __sniff(self):
        """Manage sniffing loop"""
        while self.sniff_status: #stop thread when sniff_status is FALSE
                sniff(filter=self.filter_str,prn = self.__printPackets,
                    count = 1)
                
    def __save(self):
        """Save pkt in pcap file"""
        namefile = "%s%s.cap" \
        %(self.savingdir,datetime.datetime.now().strftime("%d-%b %H:%M:%S"))
        if not self.sniff_status:
            wrpcap(namefile,self.pkt)
        else:
            self.sniff_status = False
            wrpcap(namefile,self.pkt)
        self.pkt = []
        
    def __printPackets(self,pkt):
        """Draw last packets"""
        if self.sniff_status:
            self.pkt.append(pkt)
            if len(self.pkt) > 5 and self.tab_status:
                for i in xrange(0,9):
                    self.stdscr.addstr(self.base_Y+15-i, self.base_X+1,
                        self.pkt[(len(self.pkt)-1)-i].summary(),
                            curses.color_pair(1))
            self.stdscr.refresh()                
    def __drawSaveDir(self):
        utils.drawBox(self.stdscr,self.base_Y,self.base_X+46,32,
            self.savingdir,"Saving directory")
        self.stdscr.addstr(self.base_Y,self.base_X+54,"D",curses.color_pair(2))
        self.stdscr.refresh()
        
    def __drawTabContent(self):
        #clear screen
        self.stdscr.clear()
        
        #draw textbox with label
        utils.drawBox(self.stdscr,self.base_Y,self.base_X,20,
            self.victim_ip,"Victim")
        self.stdscr.addstr(self.base_Y,self.base_X+1,"V",curses.color_pair(2))
    
        utils.drawBox(self.stdscr,self.base_Y,self.base_X+23,20,
            self.router_ip,"Router")
        self.stdscr.addstr(self.base_Y, self.base_X+24, "R",
            curses.color_pair(2))
        
        utils.drawBox(self.stdscr,self.base_Y,self.base_X+46,32,
            self.savingdir_show,"Saving directory")
        self.stdscr.addstr(self.base_Y,self.base_X+54,"D",curses.color_pair(2))
        
        utils.drawBox(self.stdscr,self.base_Y+3,self.base_X,78,
            self.filter_str,"Filter")
        self.stdscr.addstr(self.base_Y+3,self.base_X+1,"F",curses.color_pair(2))
        
        curses.textpad.rectangle(self.stdscr,
             self.base_Y+6,self.base_X, self.base_Y+16, self.base_X+78)
             
        self.stdscr.addstr(self.base_Y+6,self.base_X+1,
            "Start/Stop(and save) sniffed packets",curses.color_pair(1))
            
        self.stdscr.addstr(self.base_Y+6,self.base_X+1,"S",curses.color_pair(2))
        
        #draw sniff status
        if self.sniff_status == True:
            self.stdscr.addstr(self.base_Y+18,0, "Sniffing...",
                curses.color_pair(3))
        else:
            self.stdscr.addstr(self.base_Y+18,0, "Waiting...",
                curses.color_pair(2))
        self.stdscr.addstr(self.base_Y+17, 0, "Status:")
        
        #draw tabs navigator        
        utils.drawMenuBar(self.stdscr,self.length_win)
        self.stdscr.addstr(0, 22, "3.Sniff",curses.color_pair(3))
        self.stdscr.refresh()
