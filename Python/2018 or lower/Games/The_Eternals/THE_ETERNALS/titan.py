#### TITAN RACE ####
#### IMPORTS ####
from library import *

#### MAIN ####
class Titan():
    def __init__(self):
        self.hp = 20
        self.name = None
Titan = Titan()

def mountain():
    typewriter("Welcome to Mountain city great ruler!\nHere you will be able to rule to your fullest and no one can disobay you, or can the?\nYou decide in this City!\n")
    typewriter("But first you must decide what your ruling name will be. So go on, tell me!\n")
    rule_name = input("> ")
    if Titan.name is None:
        Titan.name = rule_name
    typewriter("Thats such a great name " + Titan.name + ". My name is eagsy,\nyour personal mage consultant, I will help you along the way.\n")
    typewriter("First off, as a Titan, you have 20 hp! Thats a lot, but you still need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 20. You can be the most feared Titan ever or the Nicest, you choose...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR MOUNTAIN

def archdale():
    typewriter("Welcome to Archdale city great ruler!\nHere you will be able to rule to your fullest and no one can disobay you, or can the?\nYou decide in this City!\n")
    typewriter("But first you must decide what your ruling name will be. So go on, tell me!\n")
    rule_name = input("> ")
    if Titan.name is None:
        Titan.name = rule_name
    typewriter("Thats such a great name " + Titan.name + ". My name is eagsy,\nyour personal mage consultant, I will help you along the way.\n")
    typewriter("First off, as a Titan, you have 20 hp! Thats a lot, but you still need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 20. You can be the most feared Titan ever or the Nicest, you choose...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR ARCHDALE

def ruckloop():
    typewriter("Welcome to Ruckloop city great ruler!\nHere you will be able to rule to your fullest and no one can disobay you, or can the?\nYou decide in this City!\n")
    typewriter("But first you must decide what your ruling name will be. So go on, tell me!\n")
    rule_name = input("> ")
    if Titan.name is None:
        Titan.name = rule_name
    typewriter("Thats such a great name " + Titan.name + ". My name is eagsy,\nyour personal mage consultant, I will help you along the way.\n")
    typewriter("First off, as a Titan, you have 20 hp! Thats a lot, but you still need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 20. You can be the most feared Titan ever or the Nicest, you choose...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR RUCKLOOP

def daisyring():
    typewriter("Welcome to Daisyring city great ruler!\nHere you will be able to rule to your fullest and no one can disobay you, or can the?\nYou decide in this City!\n")
    typewriter("But first you must decide what your ruling name will be. So go on, tell me!\n")
    rule_name = input("> ")
    if Titan.name is None:
        Titan.name = rule_name
    typewriter("Thats such a great name " + Titan.name + ". My name is eagsy,\nyour personal mage consultant, I will help you along the way.\n")
    typewriter("First off, as a Titan, you have 20 hp! Thats a lot, but you still need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 20. You can be the most feared Titan ever or the Nicest, you choose...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR DAISYRING

def titan_beginning():
    sleep(0.5)
    typewriter("Goodmorning sir! Todays the big day!\n")
    sleep(0.5)
    typewriter("Who are you?\n")
    sleep(0.5)
    typewriter("You will learn that later, for now you must get ready \n")
    sleep(0.5)
    typewriter("Can you tell me whats happening?\n")
    sleep(0.5)
    typewriter("Todays the day you get to pick your city to rule...\n")
    sleep(0.5)
    print(YELLOW)
    print("- Mountain, (military city, most hard to rule)\n")
    print("- Archdale (The biggest city in Aveleen, 2nd most difficult to rule)\n")
    print("- Ruckloop (Forrest city, 3rd most difficult to rule)\n")
    print("- Daisyring (Farming city, 4th most difficult to rule)\n")
    print(RESET_COLOR)
    while True:
        ruler_of = input("> ")
        if ruler_of.lower() not in ("archdale", "ruckloop", "daisyring", "mountain"):
            print(RED + "Please specify what place you want to rule." + RESET_COLOR)
            continue
        elif ruler_of.lower() == "archdale":
            clear()
            archdale()
            break
        elif ruler_of.lower() == "ruckloop":
            clear()
            ruckloop()
            break
        elif ruler_of.lower() == "daisyring":
            clear()
            daisyring()
            break
        elif ruler_of.lower() == "mountain":
            clear()
            mountain()
            break
        else:
            break
