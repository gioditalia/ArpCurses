import curses
import time
import curses.textpad

def drawTitle(stdscr,y,x):
    #draw title
    stdscr.addstr(y, x, "    _             ___        ",curses.color_pair(1))
    stdscr.addstr(y+1, x, "   /_\  _ _ _ __ / __|  _ _ _ ___ ___ ___",curses.color_pair(1))
    stdscr.addstr(y+2, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    
def drawPrettyTitle(stdscr,y,x,speed):
    #draw title
    stdscr.addstr(y, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+1, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+2, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+3, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)

    
    stdscr.addstr(y, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+1, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+2, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    
    stdscr.addstr(y, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+1, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+2, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y, x, "   /_\  _ _ _ __ / __|  _ _ _ ___ ___ ___",curses.color_pair(1))
    stdscr.addstr(y+2, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    stdscr.clear()
    stdscr.addstr(y+1, x, "   /_\  _ _ _ __ / __|  _ _ _ ___ ___ ___",curses.color_pair(1))
    stdscr.addstr(y+2, x, "  / _ \| '_| '_ \ (_| || | '_(_-</ -_|_-<",curses.color_pair(1))
    stdscr.addstr(y+3, x, " /_/ \_\_| | .__/\___\_,_|_| /__/\___/__/",curses.color_pair(1))
    stdscr.addstr(y+4, x, "           |_| The ArpPoisoning tool     ",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(speed)
    
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
    stdscr.addstr(y+1, x+1, (" "*(len(msg))),curses.color_pair(1)) #set color for all box
    stdscr.addstr(y+2, x+1, (" "*(len(msg))),curses.color_pair(1))
    stdscr.addstr(y+3, x+1, (" "*(len(msg))),curses.color_pair(1))
    stdscr.addstr(y+1, x+1, msg,curses.color_pair(1))   #write message
    stdscr.addstr(y+3, (x*2+len(msg))/2, "Ok",curses.color_pair(1))   #write ok
    stdscr.getkey() #wait any key

def questBox(stdscr,y,x,msg,title="questbox"):
    curses.textpad.rectangle(stdscr, y,x, y+4, len(msg)+x+1)    #draw message box
    stdscr.addstr(y, x+1, title,curses.color_pair(1)) #set box title
    stdscr.addstr(y+1, x+1, (" "*(len(msg))),curses.color_pair(1)) #set color for all box
    stdscr.addstr(y+2, x+1, (" "*(len(msg))),curses.color_pair(1))
    stdscr.addstr(y+3, x+1, (" "*(len(msg))),curses.color_pair(1))
    stdscr.addstr(y+1, x+1, msg,curses.color_pair(1))   #write message
    stdscr.addstr(y+3, ((x*2+len(msg))/2)-3, "Quit    No",curses.color_pair(1))   #write ok
    stdscr.addstr(y+3, ((x*2+len(msg))/2)-3, "Q",curses.color_pair(2))   #write ok
    stdscr.addstr(y+3, ((x*2+len(msg))/2)+5, "N",curses.color_pair(2))   #write ok
    while 1:
        digit = stdscr.getkey() #wait any key
        if digit == "q":
            return 1
        if digit == "n":
            return 0
    
def drawMenuBar(stdscr,length_win):
    stdscr.addstr(0, 0, (" "*length_win),curses.color_pair(2))
    stdscr.addstr(0, 0, "1.Attack    2.Scan    3.Sniff    4.Network    Q.Quit",curses.color_pair(2))