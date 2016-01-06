import os
import socket
from scapy.layers.l2 import arping

def firewallForwardConf(iface):
    """Forward any connection.
  
    Keyword arguments:
    iface -- the network interface
    """
    #write appropriate kernel config settings
    f = open("/proc/sys/net/ipv4/ip_forward", "w")
    f.write('1')
    f.close()
    f = open("/proc/sys/net/ipv4/conf/" + iface + "/send_redirects", "w")
    f.write('0')
    f.close()

def firewallBlockingConf(iface):
    """Block any connection 
  
    Keyword arguments:
    iface -- the network interface
    """
    #write appropriate kernel config settings
    f = open("/proc/sys/net/ipv4/ip_forward", "w")
    f.write('0')
    f.close()
    f = open("/proc/sys/net/ipv4/conf/" + iface + "/send_redirects", "w")
    f.write('1')
    f.close()





def scan(net,iface="eth0",timeout=1,verbose=0):
    """Scan a network.

    Keyword arguments:
    net -- the network you want scan (CIDR notation)
    iface -- the network interface (default "eth0")
    timeout -- time between ping of hosts (default 1)
    verbose -- set verbose mode of arping (default 0)
    
    Return values:
    List of 3-tuple (mac address,ip address,hostname)
    """
    res = []
    #ping entire network
    ans, unans = arping(net, iface=iface, timeout=timeout, verbose = verbose)
    #take only the hosts that responded
    for s, r in ans.res:
        #try to take info and put them on the list
        try:
            hostname = socket.gethostbyaddr(r.psrc)
            res.append((r.src,r.psrc,hostname[0]))
        except socket.herror:
            # failed to resolve
            res.append((r.src,r.psrc,""))
            pass
    return res
