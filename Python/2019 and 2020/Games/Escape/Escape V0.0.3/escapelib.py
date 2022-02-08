# Library for Escape game
import random
import sys
from time import sleep
from os import system
from colorama import Fore, Style, Back

# Color Vaiables
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
BLACK = Fore.BLACK
BACK_RED = Back.RED
DIM = Style.DIM
RESET_COLOR = Style.RESET_ALL

# Functions
def typewriter(string, time):
    for char in string:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()

def commands():
    print("""
================
Commands: """ + YELLOW + """
  - go """ + CYAN + """ [direction] """ + YELLOW + """
  - get """ + CYAN + """[item] """ + YELLOW  + """
  - help
  - quit """ + RESET_COLOR + """
================
        """)

def resize():
    system('mode con: cols=100 lines=30')

def clear():
    system("cls")

def banner():
    print("")
    banner = """
        ----------------------------------------------------------------------------------
        |    ▄████████    ▄████████  ▄████████    ▄████████    ▄███████▄    ▄████████    |
        |    ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   |
        |    ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀    |
        |    ███▄▄▄       ███        ███          ███    ███   ███    ███  ▄███▄▄▄       |
        |    ███▀▀▀     ▀███████████ ███        ▀███████████ ▀█████████▀  ▀▀███▀▀▀       |
        |    ███    █▄           ███ ███    █▄    ███    ███   ███          ███    █▄    |
        |    ███    ███    ▄█    ███ ███    ███   ███    ███   ███          ███    ███   |
        |    ██████████  ▄████████▀  ████████▀    ███    █▀   ▄████▀        ██████████   |
        ----------------------------------------------------------------------------------
                                   Made By: Parker Cranfield
"""
    x = banner
    print(RED + x + RESET_COLOR, 0.00000000001)
