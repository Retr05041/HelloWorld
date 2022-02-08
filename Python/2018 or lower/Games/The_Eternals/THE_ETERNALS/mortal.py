#### MORTAL RACE ####
#### IMPORTS ####
from library import *

#### MAIN ####
class Mortal():
    def __init__(self):
        self.hp = 5
        self.name = None
Mortal = Mortal()


def mountain():
    typewriter("Welcome to Mountain city, Here you will try to survive this as you try to accomplish your dreams.\nYou better get working, or you might not live to see another day\n")
    typewriter("To be part of this city, you must register under a name...")
    mortal_name = input("> ")
    if Mortal.name is None:
        Mortal.name = mortal_name
    typewriter("Great " + Mortal.name + ". You have now been exepted.\n")
    typewriter("First off, as a mortal, you have 5 hp. You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 5. You could live your life as a good working soal, or choose to begin a rebelliion...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR MOUNTAIN

def archdale():
    typewriter("Welcome to Archdale city, Here you will try to survive this as you try to accomplish your dreams.\nYou better get working, or you might not live to see another day\n")
    typewriter("To be part of this city, you must register under a name...")
    mortal_name = input("> ")
    if Mortal.name is None:
        Mortal.name = mortal_name
    typewriter("Great " + Mortal.name + ". You have now been exepted.\n")
    typewriter("First off, as a mortal, you have 5 hp. You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 5. You could live your life as a good working soal, or choose to begin a rebelliion...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR ARCHDALE

def ruckloop():
    typewriter("Welcome to Ruckloop city, Here you will try to survive this as you try to accomplish your dreams.\nYou better get working, or you might not live to see another day\n")
    typewriter("To be part of this city, you must register under a name...")
    mortal_name = input("> ")
    if Mortal.name is None:
        Mortal.name = mortal_name
    typewriter("Great " + Mortal.name + ". You have now been exepted.\n")
    typewriter("First off, as a mortal, you have 5 hp. You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 5. You could live your life as a good working soal, or choose to begin a rebelliion...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR RUCKLOOP

def daisyring():
    typewriter("Welcome to Daisyring city, Here you will try to survive this as you try to accomplish your dreams.\nYou better get working, or you might not live to see another day\n")
    typewriter("To be part of this city, you must register under a name...")
    mortal_name = input("> ")
    if Mortal.name is None:
        Mortal.name = mortal_name
    typewriter("Great " + Mortal.name + ". You have now been exepted.\n")
    typewriter("First off, as a mortal, you have 5 hp. You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 5. You could live your life as a good working soal, or choose to begin a rebelliion...\nGood luck!")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR DAISYRING

def mortal_beginning():
    print("Welcome mage")
    sleep(0.5)
    typewriter("Hey there friend! welcome to Aveleen, where most of our dreams come true!\n")
    sleep(0.5)
    typewriter("Really?!\n")
    sleep(0.5)
    typewriter("Shh, if you really want to know, you gotta know someone to actually get rich, like a mage or Titan... but thats rare\n")
    sleep(0.5)
    typewriter("Well, How do I befriend one of those?\n")
    sleep(0.5)
    typewriter("Head to one of the citys and go from there, heres a list of them...\n")
    sleep(0.5)
    print(YELLOW)
    print("- Mountain, (military city, most hard to rule)\n")
    print("- Archdale (The biggest city in Aveleen, 2nd most difficult to rule)\n")
    print("- Ruckloop (Forrest city, 3rd most difficult to rule)\n")
    print("- Daisyring (Farming city, 4th most difficult to rule)\n")
    print(RESET_COLOR)
    while True:
        mortal_of = input("> ")
        if mortal_of.lower() not in ("archdale", "ruckloop", "daisyring", "mountain"):
            print(RED + "Please specify what place you want to serve." + RESET_COLOR)
            continue
        elif mortal_of.lower() == "archdale":
            clear()
            archdale()
            break
        elif mortal_of.lower() == "ruckloop":
            clear()
            ruckloop()
            break
        elif mortal_of.lower() == "daisyring":
            clear()
            daisyring()
            break
        elif mortal_of.lower() == "mountain":
            clear()
            mountain()
            break
        else:
            break
