import subprocess
from colorama import Fore

print(f"{Fore.BLUE}[1] Port Scanner.\n[2] BoganBuster (web dir searcher).\n[3] DDOS a target.\n[4] Proxy Checker and gen.")
print('\n')

option = input('Please enter a number: ')

if option == '1':
    from Modules.port_scanner import start_scan
    start_scan()

if option == '2':
    from Modules.BoganBuster import start_all
    start_all()

if option == '3':
    from Modules.ddos import start_all
    start_all()

if option == '4':
    from Modules.proxy_checker import start
    start()
