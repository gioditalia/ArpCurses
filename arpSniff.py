import curses
import utils
import datetime
import threading
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
        
        self.savedir = utils.makeTextBox(self.base_Y,self.base_X+50,32)
        self.savingdir = "./"
        
    def main(self,victim,router):

        self.victim_ip = victim.gather().split(" ")[0] #victim address
        self.router_ip = router.gather().split(" ")[0] #router address
        self.tab_status = True #enable write sniff packets
     
        while 1:
            self.__drawTabContent()
            
            #wait key's pression
            digit = self.stdscr.getkey()
            
            #arpcurses generic menu
            if digit == "1" or digit == "2" or digit == "4" or digit == "q":
                self.tab_status = False #disable write sniff packets
                return digit
            
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
                            utils.infoBox(self.stdscr,self.base_Y+1,self.base_X+1,
                                " Something going wrong, control your settings ","Error!")
                    else:
                        if utils.saveBox(self.stdscr,6,15,
                            "Save sniffed packets in .cap file?",""):
                            self.__save()
              
            if digit == "d":
                self.savingdir = self.savedir.edit().split(" ")[0]

    def __sniff(self):
        """Manage sniffing loop"""
        filter_str = "host %s" %(self.victim_ip)
        while self.sniff_status: #stop thread when attack_status is FALSE
            sniff(filter=filter_str,prn = self.__printPackets,count = 1)
            
    def __save(self):
        """Save pkt in pcap file"""
        namefile = "%s%s.cap" %(self.savingdir,datetime.datetime.now().strftime("%d-%b %H:%M:%S"))
        if not self.sniff_status:
            wrpcap(namefile,self.pkt)
        else:
            self.sniff_status = False
            wrpcap(namefile,self.pkt)
        self.pkt = []
        
    def __printPackets(self,pkt):
        """Draw last 10 packets"""
        if self.sniff_status:
            self.pkt.append(pkt)
            if len(self.pkt) > 5 and self.tab_status:
                for i in xrange(0,10):
                    self.stdscr.addstr(self.base_Y+15-i, self.base_X+1,
                        self.pkt[(len(self.pkt)-1)-i].summary(),
                            curses.color_pair(1))
            self.stdscr.refresh()                
                
    def __drawTabContent(self):
        #clear screen
        self.stdscr.clear()
        
        #draw textbox with label
        utils.drawBox(self.stdscr,self.base_Y,self.base_X,20,
            self.victim_ip,"Victim")
    
        utils.drawBox(self.stdscr,self.base_Y,self.base_X+23,20,
            self.router_ip,"Router")
        
        utils.drawBox(self.stdscr,self.base_Y,self.base_X+46,32,
            self.savingdir,"Saving directory")
        self.stdscr.addstr(self.base_Y,self.base_X+58,"D",curses.color_pair(2))
        
        curses.textpad.rectangle(self.stdscr,
             self.base_Y+4,self.base_X, self.base_Y+16, self.base_X+78)
             
        self.stdscr.addstr(self.base_Y+4,self.base_X+1,
            "Start/Stop(and save) sniffed packets",curses.color_pair(1))
            
        self.stdscr.addstr(self.base_Y+4,self.base_X+1,"S",curses.color_pair(2))
        
        #draw sniff status
        if self.sniff_status == True:
            self.stdscr.addstr(self.base_Y+18,0, "Sniffing...",curses.color_pair(3))
        else:
            self.stdscr.addstr(self.base_Y+18,0, "Waiting...",curses.color_pair(2))
        self.stdscr.addstr(self.base_Y+17, 0, "Status:")
        
        #draw tabs navigator        
        utils.drawMenuBar(self.stdscr,self.length_win)
        self.stdscr.addstr(0, 22, "3.Sniff",curses.color_pair(3))
        self.stdscr.refresh()
