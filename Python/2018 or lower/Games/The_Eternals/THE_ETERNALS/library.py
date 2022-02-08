#### IMPORTS ####
import sys
import time
from time import sleep
import random
import math
import time
from time import sleep
import os
from os import system
import colorama
from colorama import Fore, Style
from pygame import mixer

#### INITS ####
colorama.init()
mixer.init()

#### VARIABLES ####
global RED
global GREEN
global CYAN
global YELLOW
global RESET_COLOR
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET_COLOR = Style.RESET_ALL

#### FUNCTIONS ####
def music():
    mixer.music.load("walk_alone.mp3")
    mixer.music.play(-1)

def size():
    sys.stdout.write("\x1b[8;30;116t")

def typewriter(str, time = 0.05):
    for char in str:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()

def background():
    print(YELLOW)
    print("  ________  __    __  ________        ________  ________  ________  _______   __    __   ______   __         ______  ")
    sleep(0.1)
    print(" /        |/  |  /  |/        |      /        |/        |/        |/       \ /  \  /  | /      \ /  |       /      \ ")
    sleep(0.1)
    print(" $$$$$$$$/ $$ |  $$ |$$$$$$$$/       $$$$$$$$/ $$$$$$$$/ $$$$$$$$/ $$$$$$$  |$$  \ $$ |/$$$$$$  |$$ |      /$$$$$$  |")
    sleep(0.1)
    print("    $$ |   $$ |__$$ |$$ |__          $$ |__       $$ |   $$ |__    $$ |__$$ |$$$  \$$ |$$ |__$$ |$$ |      $$ \__$$/ ")
    sleep(0.1)
    print("    $$ |   $$    $$ |$$    |         $$    |      $$ |   $$    |   $$    $$< $$$$  $$ |$$    $$ |$$ |      $$      \ ")
    sleep(0.1)
    print("    $$ |   $$$$$$$$ |$$$$$/          $$$$$/       $$ |   $$$$$/    $$$$$$$  |$$ $$ $$ |$$$$$$$$ |$$ |       $$$$$$  |")
    sleep(0.1)
    print("    $$ |   $$ |  $$ |$$ |_____       $$ |_____    $$ |   $$ |_____ $$ |  $$ |$$ |$$$$ |$$ |  $$ |$$ |_____ / \__$$ | ")
    sleep(0.1)
    print("    $$ |   $$ |  $$ |$$       |      $$       |   $$ |   $$       |$$ |  $$ |$$ | $$$ |$$ |  $$ |$$       |$$    $$/ ")
    sleep(0.1)
    print("    $$/    $$/   $$/ $$$$$$$$/       $$$$$$$$/    $$/    $$$$$$$$/ $$/   $$/ $$/   $$/ $$/   $$/ $$$$$$$$/  $$$$$$/\n")
    print(CYAN)
    print("                                               MADE BY PARKER CRANFIELD                                            \n")
    print("                                           'Walk Alone' - Fearless Motivation                                      \n")
    print(RESET_COLOR)

def clear():
    system("cls")
