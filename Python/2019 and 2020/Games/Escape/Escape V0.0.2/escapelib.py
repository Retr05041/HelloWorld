# Library for Escape game
import random
import sys
from time import sleep
from os import system
from colorama import Fore, Style

RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
RESET_COLOR = Style.RESET_ALL

def typewriter(string, time):
    for char in string:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()

def commands():
    print("""
================
Commands: """ + YELLOW + """
  go """ + CYAN + """ [direction] """ + YELLOW + """
  get """ + CYAN + """[item] """ + RESET_COLOR + """
================
        """)

def resize():
    system('mode con: cols=100 lines=30')

def clear():
    system("cls")

def banner():
    print("")
    banner = """
           ▄████████    ▄████████  ▄████████    ▄████████    ▄███████▄    ▄████████
          ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███
          ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀
         ▄███▄▄▄       ███        ███          ███    ███   ███    ███  ▄███▄▄▄
        ▀▀███▀▀▀     ▀███████████ ███        ▀███████████ ▀█████████▀  ▀▀███▀▀▀
          ███    █▄           ███ ███    █▄    ███    ███   ███          ███    █▄
          ███    ███    ▄█    ███ ███    ███   ███    ███   ███          ███    ███
          ██████████  ▄████████▀  ████████▀    ███    █▀   ▄████▀        ██████████
            """
    x = banner.center(50)
    typewriter(RED + x + RESET_COLOR, 0.00000000001)
