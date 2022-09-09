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

from base64 import decode
from cgitb import text
from datetime import date, datetime
from ensurepip import version
from fileinput import close
from hmac import digest
from importlib.resources import as_file
from posixpath import split
from os import name, system
from secrets import choice
from pystyle import Colors, Colorate
import sys
import os
import time
import random
import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import subprocess, requests
import os, hashlib, os.path, time
from threading import Thread
from multiprocessing import Process
from requests import get

from pystyle import Colorate, Center, Write, Anime, Colors, System, Col

# IP blaclist 
blacklistip = ['1.1.1.1', 'enter-ip-for-blacklist-him']
invalidip = ['']
invalidport = ['']
invalidtime = ['']

ts = time.sleep



if name == 'nt':
    system("title Wxny - Botnet ( Connected to server : EU-06 )")

    print(Fore.CYAN + "                                               Wxny By Urkaaz#3335    ")

print("       ")
print("       ")
LicenseKey = Write.Input("Entrez la clé pour l'accès Wxny : ", Colors.red_to_purple, interval=0.0025)
print("       ")
if LicenseKey == "wxny":
    print(Fore.GREEN + "La clé est valide !")
    time.sleep(0.5)
    os.system("cls")
else:
    print(Fore.RED + "La clé est invalide")
    print("       ")
    print(Fore.RED + "Appuyez sur enter pour fermer Wxny Botnet")
    input("")
    exit(123)
    

print(Center.XCenter (Fore.RED + """ __        __                   ____        _              _   
 \ \      / /_  ___ __  _   _  | __ )  ___ | |_ _ __   ___| |_ 
  \ \ /\ / /\ \/ / '_ \| | | | |  _ \ / _ \| __| '_ \ / _ \ __|
   \ V  V /  >  <| | | | |_| | | |_) | (_) | |_| | | |  __/ |_ 
    \_/\_/  /_/\_\_| |_|\__, | |____/ \___/ \__|_| |_|\___|\__|
                        |___/                                  """))

print("    ")


ip = Write.Input("""╔[root@wxny]
║
╚═══════> """, Colors.red_to_purple, interval=0.0025)
if ip in blacklistip:
        os.system("cls")
        print(Fore.RED + """
███████╗██████╗░██████╗░░█████╗░██████╗░  ██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██║
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝  ██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗  ╚═╝
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ██╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝""")
        print("     ")
        print(Fore.RED + "Action impossible, l'adresse IP est blacklist de Wxny en raison de sécurité")
        print("       ")
        print(Fore.RED + "Appuyez sur enter pour fermer Wxny Botnet")
        input("")
        exit(123)

if ip in invalidip:
        os.system("cls")
        print(Fore.RED + """
███████╗██████╗░██████╗░░█████╗░██████╗░  ██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██║
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝  ██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗  ╚═╝
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║  ██╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝""")
        print("     ")
        print(Fore.RED + "L'adresse IP n'existe pas")
        print("       ")
        print(Fore.RED + "Appuyez sur enter pour fermer Wxny Botnet")
        input("")
        exit(123) 


else:
    print("     ")
    port = Write.Input("""╔[port@wxny]
║
╚═══════> """, Colors.blue_to_purple, interval=0.0025)
    print("     ")
    temps = Write.Input("""╔[time@wxny]
║
╚═══════> """, Colors.blue_to_cyan, interval=0.0025)
    

print("    ")
ts(2)
print("     ")
print(Fore.LIGHTMAGENTA_EX + "La connexion à réussie !")
ts(1)

if name == 'nt':
    system(f"title Wxny - Botnet - Target : {ip} - Port : {port} - Time : {temps} ")
    
os.system("cls")


print(Center.XCenter (Fore.RED + """ __        __                   ____        _              _   
 \ \      / /_  ___ __  _   _  | __ )  ___ | |_ _ __   ___| |_ 
  \ \ /\ / /\ \/ / '_ \| | | | |  _ \ / _ \| __| '_ \ / _ \ __|
   \ V  V /  >  <| | | | |_| | | |_) | (_) | |_| | | |  __/ |_ 
    \_/\_/  /_/\_\_| |_|\__, | |____/ \___/ \__|_| |_|\___|\__|
                        |___/                                  """))

print("    ")

print(Fore.MAGENTA + f"""╔═══════════════════════════════════════════
║ TARGET    : [{ip}] 
║ PORT      : [{port}]
║ TIME      : [{temps} s]
║ GBPS      : [100 GBPS/S]
║ METHOD    : [{ip}]
╚═══════════════════════════════════════════""",)

print("    ")
print(Fore.CYAN + f"""╔══════════════════════════════════════════════════
║ TOTAL NETWORK ATTACKS: [145+] 
╚══════════════════════════════════════════════════""")

print("    ")
print(Fore.BLUE + f"""╔══════════════════════════════════════════════════
║ Copyright Superior 2022 All Rights Reserved  
╚══════════════════════════════════════════════════""")
print("    ")
print(Fore.BLUE + f"""╔══════════════════════════════════════════════════
║ Enter X for stop attack  
╚══════════════════════════════════════════════════""")

input("")
os.system("cls")
if name == 'nt':
    system(f"title Wxny - Botnet - Attack finish ")
print(Fore.GREEN + f"""                              ─════════════════════════════════════════════════════─
               	                                     Attack finish
                              ─════════════════════════════════════════════════════─""")
print("    ")
print(Fore.LIGHTCYAN_EX + "                                 Appuyez sur enter pour fermer Wxny Botnet")
input("")
exit(123)

ts(12000)
