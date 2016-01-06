import curses
import utils


class ArpSniff():

    def __init__(self,stdscr,interface):
        
        self.base_X = 1
        self.base_Y = 2
        self.length_win = 85
        self.stdscr = stdscr
        

        self.interface = interface #physical interface
        
    def main(self,victim,router):
     
     
        while 1:
            self.__drawTabContent()
            
            #wait key's pression
            digit = self.stdscr.getkey()
            
            #arpcurses generic menu
            if digit == "1" or digit == "2" or digit == "4" or digit == "q":
                return digit
                
                
                
    def __drawTabContent(self):
        #clear screen
        self.stdscr.clear()


        #draw tabs navigator        
        utils.drawMenuBar(self.stdscr,self.length_win)
        self.stdscr.addstr(0, 22, "3.Sniff",curses.color_pair(3))
        self.stdscr.refresh()
