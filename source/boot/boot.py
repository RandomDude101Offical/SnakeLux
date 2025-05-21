# i hope this'll work properly
# functions: begtext, begdata, begbss, endtext, enddata, endbss

def begtext():
  data()
def begdata():
  bss()
def begbss():
  text()

SYSSIZE = 0x0900 # idk what's syssize value is so we'll stick with this

BOOTSEG = 0x07c0
INITSEG = 0x9000
SYSSEG  = 0x1000
ENDSEG	= SYSSEG + SYSSIZE

start()
def start():
  ax = BOOTSEG
  ds = ax
  ax = INITSEG
  es = ax
  cx = 256 # ???
  si = si - si
  di = di - di
  # supposed "MOVW" function (i couldn't find any arguments
  # supposed "REP" function (also no functions)
  go()

def go():
  
  

# !! THIS IS NOT FINISHED !!
