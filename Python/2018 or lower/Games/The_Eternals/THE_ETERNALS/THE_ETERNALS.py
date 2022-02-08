#   THE ETERNALS
#   Written in python 3+
#   By: Parker Cranfield
#   04/27/2019

#### IMPORTS ####
from library import *
from titan import *
from mage import *
from mortal import *

#### MAIN ####
def start():
    sleep(0.5)
    typewriter("Welcome to the great country of Aveleen! Where you can either be a ruler of a city!\nA mystical mage! Or a pure hearted mortal!\n")
    sleep(0.5)
    typewriter("What race would you like to be? Choose wisely...\n")
    sleep(0.5)
    print(YELLOW)
    print("- TITAN (ruler)\n")
    print("- MAGE (consultant to titans)\n")
    print("- MORTAL (citizens of Aveleen)\n")
    print(RESET_COLOR)
    while True:
        race = input("> ")
        if race.lower() not in ("titan", "mage", "mortal"):
            print(RED + "Please specify what race you want to be." + RESET_COLOR)
            continue
        elif race.lower() == "titan":
            clear()
            titan_beginning()
            break
        elif race.lower() == "mage":
            clear()
            mage_beginning()
            break
        elif race.lower() == "mortal":
            clear()
            mortal_beginning()
            break
        else:
            break

def main():
    size()
    clear()
    music()
    background()
    typewriter("Ready to start?\n")
    print(YELLOW)
    print("- Yes\n")
    print("- No\n" + RESET_COLOR)
    while True:
        ready = input("> ")
        if ready.lower() not in ("yes", "no"):
            print(RED + "Please specify wheather you want to start." + RESET_COLOR)
            continue
        elif ready.lower() == "yes":
            system("cls")
            start()
        elif ready.lower() == "no":
            exit()
        else:
            break
if __name__ == "__main__":
    main()
