import threading
import time
from colorama import init, Fore
import ctypes
import string
import random

init(convert=True)
ctypes.windll.kernel32.SetConsoleTitleW("Gift card Generator by SLARNVIKOVX")
title = '''
   _____ _               _____  _   ___      _______ _  ________      ____   __
  / ____| |        /\   |  __ \| \ | \ \    / /_   _| |/ / __ \ \    / /\ \ / /
 | (___ | |       /  \  | |__) |  \| |\ \  / /  | | | ' / |  | \ \  / /  \ V / 
  \___ \| |      / /\ \ |  _  /| . ` | \ \/ /   | | |  <| |  | |\ \/ /    > <  
  ____) | |____ / ____ \| | \ \| |\  |  \  /   _| |_| . \ |__| | \  /    / . \ 
 |_____/|______/_/    \_\_|  \_\_| \_|   \/   |_____|_|\_\____/   \/    /_/ \_\
                                                                               
                                                                               
                               ░                                                      
'''

print(Fore.GREEN + title + Fore.WHITE)
f = open('Codes.txt', 'a')
print()
print(Fore.RED + 'Enter amount of codes to generate: ')
amount = int(input())
fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13))
    f.write(code.upper() + '\n')
    print(Fore.GREEN + code.upper())
    fix += 1
    ctypes.windll.kernel32.SetConsoleTitleW("Generated Codes: " + str(fix) + "/" + str(amount))
