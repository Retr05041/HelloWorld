# Library for Escape game
import random
import sys
from pygame import mixer
from time import sleep
from os import system
from colorama import Fore, Style, Back

# inits
mixer.init()

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
def music():
    mixer.music.load("scarymusic.mp3")
    mixer.music.play(-1)

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
                            Music: Scary Horror Music - Haunted
"""
    x = banner
    print(RED + x + RESET_COLOR)

def ending():
    clear()
    print("")
    endbanner = """
        ------------------------------------------------------------------------
        |     ▄█     █▄   ▄█  ███▄▄▄▄   ███▄▄▄▄      ▄████████    ▄████████    |
        |    ███     ███ ███  ███▀▀▀██▄ ███▀▀▀██▄   ███    ███   ███    ███    |
        |    ███     ███ ███▌ ███   ███ ███   ███   ███    █▀    ███    ███    |
        |    ███     ███ ███▌ ███   ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀    |
        |    ███     ███ ███▌ ███   ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀      |
        |    ███     ███ ███  ███   ███ ███   ███   ███    █▄  ▀███████████    |
        |    ███ ▄█▄ ███ ███  ███   ███ ███   ███   ███    ███   ███    ███    |
        |     ▀███▀███▀  █▀    ▀█   █▀   ▀█   █▀    ██████████   ███    ███    |
        |                                                        ███    ███    |
        ------------------------------------------------------------------------
    """
    x = endbanner
    for i in range(1, 20):
        print(RED + x)
        clear()
        print(YELLOW + x)
        clear()
    print("Good for you... Now go away")
    sleep(2)
    exit()
