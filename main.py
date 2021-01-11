#Author: KV5d
#Date: 12/2020
#Desc: Clears all temporary files on the Windows 10 operating system


#imports
import os
import shutil
from os.path import expanduser
from art import tprint
from tqdm import trange
from time import sleep
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)


#glob var
now = datetime.now()

cRes = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yell = Fore.YELLOW
blue = Fore.BLUE
purp = Fore.MAGENTA
cyan = Fore.CYAN

def space():
	print()


#intro
def intro():
	space()
	space()
	tprint("Clear")
	space()
	print(cyan + "version - 2.1.2021")
	space()
	print(now)
	space()

	for i in trange(10):
		sleep(0.001)

	space()


#main
def main0():
	while True:
		home = expanduser("~")

		tmp0 = os.path.join(home , "AppData\\Local\\Temp")
		tmp1 = r'c:\\Windows\\Temp'
		dl = os.path.join(home, "Downloads")
		donemsg = "Done!\n"

		print(red + "About to delete all temporary files!\n")
		if input("Do you want to continue [y/n]: ") != "y":
			space()
			print(green + donemsg)
			break
		space()

		shutil.rmtree(tmp0, ignore_errors=True)
		if os.path.exists(tmp0) == True:
			pass
		if os.path.exists(tmp0) == False:
			os.makedirs(tmp0)

		shutil.rmtree(tmp1, ignore_errors=True)
		if os.path.exists(tmp1) == True:
			pass
		if os.path.exists(tmp1) == False:
			os.makedirs(tmp1)

		print(red + "About to clear your downloads folder too?\n")
		if input("Do you want to continue [y/n]: ") != "y":
			space()
			print(green + donemsg)
			break
		space()

		shutil.rmtree(dl, ignore_errors=True)
		if os.path.exists(dl) == True:
			pass
		if os.path.exists(dl) == False:
			os.makedirs(dl)

		for i in trange(10):
			sleep(0.01)
		space()

		print(green + donemsg)
		print(now)
		space()
		print(cyan + "ALL SELECTED FILES HAVE BEEN REMOVED!\n")
		break


def run():
	intro()
	sleep(0.1)
	main0()
	sleep(0.1)
	input("press ENTER to exit")


run()