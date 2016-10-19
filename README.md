# ArpCurses
### A scapy-based arp poisoning with curses interface.
###### Compatible only with GNU/Linux (IPTABLES required)

## About
There are several tools much more comprehensive and flexible than this, but I wrote this software because I wanted something for everyone.
That does three simple things:
* Network scan
* arp poisoning (with optional redirection to a proxy :smiling_imp:injection:smiling_imp:)
* sniffing

## How to use
Download source

```
git clone https://github.com/gioditalia/ArpCurses.git
cd ArpCurses
```

Get root privileges

```
su
```

or

```
sudo su
```

Install requirements and run!

```
pip install -r requirements.txt
./main
```

**Note:** *You must have a root permission to use this tool properly*
