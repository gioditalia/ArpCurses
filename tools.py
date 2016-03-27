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

import socket
import platform
import os
from scapy.layers.l2 import arping

def firewallForwardConf(iface):
    """Forward any connection.
  
    Keyword arguments:
    iface -- the network interface
    """
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
    f = open("/proc/sys/net/ipv4/ip_forward", "w")
    f.write('0')
    f.close()
    f = open("/proc/sys/net/ipv4/conf/" + iface + "/send_redirects", "w")
    f.write('1')
    f.close()

def enableIptables(iface,ports,host):
    os.system("/sbin/iptables --flush")
    os.system("/sbin/iptables -t nat --flush")
    os.system("/sbin/iptables --zero")
    os.system("/sbin/iptables -A FORWARD --in-interface " +
     iface + " -j ACCEPT")
    os.system("/sbin/iptables -t nat --append POSTROUTING --out-interface " +
     iface + " -j MASQUERADE")
    #forward 80,443 to our proxy
    for port in ports:
        os.system("/sbin/iptables -t nat -A PREROUTING -p tcp --dport " +
         port + " --jump DNAT --to-destination " + host)
        open("/home/inna/ciao","a").write(port)
    
def disableIptables():
    os.system("/sbin/iptables --flush")
    os.system("/sbin/iptables -t nat --flush")
    os.system("/sbin/iptables --zero")

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
