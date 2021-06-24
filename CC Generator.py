import os
import sys

import colorama
from colorama import init, Fore
init(convert=True)

import requests
import json

import string
import random

import time
import datetime

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW(f"CC Generator | github.com/xdecemberrr")

class Gen:
    def __init__(self):
        self._n = "123456789"
        self._l = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self._m = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        self._y = ["2022", "2023", "2024", "2025", "2026"]
        self._b = ['401903', '402400', '402402', '403200', '404025', '404025', '405025', '405225', '405209', '406025', '407000', '407129', '411427', '412174', '412185', '412352', '412825', '416818', '413125', '417025', '417129', '418825', '421125', '421525', '422591', '422625', '423125', '423225', '423725', '424125', '425043', '425330', '425451', '426225', '427138', '430225', '431068', '431225', '431301', '431663', '431772', '432125', '433213', '433222', '434925', '436800', '438733', '438760', '440121', '440862', '441712', '442813', '442843', '442882', '443600', '444825', '461652', '462625', '464625', '467225', '467362', '467807', '467808', '468120', '469625', '471825', '473425', '480012', '481125', '482525', '489725', '492925']


    def get_letter(self):
        return random.choice(self._g)

    def get_number(self):
        return random.choice(self._n)

    def get_card(self):
        c = ""
        for x in range(10):
            c += random.choice(self._n)
        return c

    def get_cvv(self):
        c = ""
        for x in range(3):
            c += random.choice(self._n)
        return c

    def get_month(self):
        return random.choice(self._m)

    def get_year(self):
        return random.choice(self._y)

    def get_bin(self):
        return random.choice(self._b)


b = Gen()

def main():
    os.system('cls')
    sc = f'''
    {Fore.YELLOW}  ______     ______
     .' ___  |  .' ___  |
    / .'   \_| / .'   \_|
    | |        | |
    \ `.___.'\ \ `.___.'\  {Fore.LIGHTYELLOW_EX}github.com/xdecemberrr {Fore.YELLOW}| {Fore.LIGHTMAGENTA_EX} lel {Fore.YELLOW}
     `.____ .'  `.____ .'
    '''
    print(sc)
    print()
    accs = '''
    .1 Generate with BINS
    .2 Generate without BINS
    '''
    print(accs)
    o = input(f"    {Fore.YELLOW}.$ {Fore.LIGHTYELLOW_EX}")
    if o == "1":
        x = input(f'    {Fore.YELLOW}.$ CC Bins: {Fore.LIGHTYELLOW_EX}')
        if len(x) == 6:
            bins = x
        elif len(x) == 4:
            bins = x + b.get_number() + b.get_number()

        else:
            print(f"    {Fore.YELLOW}.$ {Fore.LIGHTRED_EX}Invalid BIN")
            time.sleep(3)
            main()

        a = int(input(f"    {Fore.YELLOW}.$ Amount: {Fore.LIGHTYELLOW_EX}"))
        print(f"    {Fore.YELLOW}.$ Loading ...")
        f = open("CC Generated.cc", "a+")
        for x in range(a):
            cvv = b.get_cvv()
            month = b.get_month()
            year = b.get_year()
            card = bins + b.get_card()
            f.write(f"{card}|{month}|{year}|{cvv}\n")
        f.close()
        print(f"    {Fore.YELLOW}.$ {Fore.LIGHTGREEN_EX}Finished")
        time.sleep(5)
        main()
    if o == "2":
        bins = b.get_bin()

        a = int(input(f"    {Fore.YELLOW}.$ Amount: {Fore.LIGHTYELLOW_EX}"))
        print(f"    {Fore.YELLOW}.$ Loading ...")
        f = open("CC Generated.cc", "a+")
        for x in range(a):
            cvv = b.get_cvv()
            month = b.get_month()
            year = b.get_year()
            card = bins + b.get_card()
            f.write(f"{card}|{month}|{year}|{cvv}\n")
        f.close()
        print(f"    {Fore.YELLOW}.$ {Fore.LIGHTGREEN_EX}Finished")
        time.sleep(5)
        main()
        
    else:
        print(f"    {Fore.YELLOW}.$ {Fore.LIGHTRED_EX}Invalid Choice")
        time.sleep(3)
        main()



if __name__ == '__main__':
    main()
