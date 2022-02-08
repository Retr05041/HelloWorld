#### MAGE RACE ####
#### IMPORTS ####
from library import *

#### MAIN ####
class Mage():
    def __init__(self):
        self.hp = 20
        self.name = None
Mage = Mage()

def mountain():
    typewriter("Welcome to Mountain city, You will serve your Titan greatly, but, beware your power, you wouldnt want to harm him or others...\n")
    typewriter("As your Titans consultant you will do his dirty work, his bidding and his maintenance...\nbut we must figure out a name for you, please pick one with great diligence\n")
    mage_name = input("> ")
    if Mage.name is None:
        Mage.name = mage_name
    typewriter("Thanks for picking so quick " + Mage.name + ". Your Titan does not like to be kept waiting\n")
    typewriter("First off, as a Mage, you have 10 hp! You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 10. You could live your life as a simple mage ever or overthrough your Titan, you choose...\nGood luck!")
    typewriter("Sincerly: High Mage of Aveleen")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR MOUNTAIN

def archdale():
    typewriter("Welcome to Archdale city, You will serve your Titan greatly, but, beware your power, you wouldnt want to harm him or others...\n")
    typewriter("As your Titans consultant you will do his dirty work, his bidding and his maintenance...\nbut we must figure out a name for you, please pick one with great diligence\n")
    mage_name = input("> ")
    if Mage.name is None:
        Mage.name = mage_name
    typewriter("Thanks for picking so quick " + Mage.name + ". Your Titan does not like to be kept waiting\n")
    typewriter("First off, as a Mage, you have 10 hp! You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 10. You could live your life as a simple mage ever or overthrough your Titan, you choose...\nGood luck!")
    typewriter("Sincerly: High Mage of Aveleen")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR ARCHDALE

def ruckloop():
    typewriter("Welcome to Ruckloop city, You will serve your Titan greatly, but, beware your power, you wouldnt want to harm him or others...\n")
    typewriter("As your Titans consultant you will do his dirty work, his bidding and his maintenance...\nbut we must figure out a name for you, please pick one with great diligence\n")
    mage_name = input("> ")
    if Mage.name is None:
        Mage.name = mage_name
    typewriter("Thanks for picking so quick " + Mage.name + ". Your Titan does not like to be kept waiting\n")
    typewriter("First off, as a Mage, you have 10 hp! You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 10. You could live your life as a simple mage ever or overthrough your Titan, you choose...\nGood luck!")
    typewriter("Sincerly: High Mage of Aveleen")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR RUCKLOOP

def daisyring():
    typewriter("Welcome to Daisyring city, You will serve your Titan greatly, but, beware your power, you wouldnt want to harm him or others...\n")
    typewriter("As your Titans consultant you will do his dirty work, his bidding and his maintenance...\nbut we must figure out a name for you, please pick one with great diligence\n")
    mage_name = input("> ")
    if Mage.name is None:
        Mage.name = mage_name
    typewriter("Thanks for picking so quick " + Mage.name + ". Your Titan does not like to be kept waiting\n")
    typewriter("First off, as a Mage, you have 10 hp! You need to watch out for bad choices.\nThose will make you loose health, the bigger the mistake, the more health lost.\n")
    typewriter("If you made good choices, your health will go up but wont go over 10. You could live your life as a simple mage ever or overthrough your Titan, you choose...\nGood luck!")
    typewriter("Sincerly: High Mage of Aveleen")
    go = input(YELLOW + "Press anything to continue." + RESET_COLOR)
    #CONTENT FOR DAISYRING

def mage_beginning():
    print("Welcome mage")
    sleep(0.5)
    typewriter("As the brotherhood of mages has done before, we welcome our new recruit\n")
    sleep(0.5)
    typewriter("I dont think I'm ready...\n")
    sleep(0.5)
    typewriter("Of course you are. You must now go forth and pick your future\n")
    sleep(0.5)
    typewriter("how will I know if its the right future\n")
    sleep(0.5)
    typewriter("My child, you must now pick what city you will serve for... you will not be asked again...\n")
    sleep(0.5)
    print(YELLOW)
    print("- Mountain, (military city, most hard to rule)\n")
    print("- Archdale (The biggest city in Aveleen, 2nd most difficult to rule)\n")
    print("- Ruckloop (Forrest city, 3rd most difficult to rule)\n")
    print("- Daisyring (Farming city, 4th most difficult to rule)\n")
    print(RESET_COLOR)
    while True:
        mage_of = input("> ")
        if mage_of.lower() not in ("archdale", "ruckloop", "daisyring", "mountain"):
            print(RED + "Please specify what place you want to serve." + RESET_COLOR)
            continue
        elif mage_of.lower() == "archdale":
            clear()
            archdale()
            break
        elif mage_of.lower() == "ruckloop":
            clear()
            ruckloop()
            break
        elif mage_of.lower() == "daisyring":
            clear()
            daisyring()
            break
        elif mage_of.lower() == "mountain":
            clear()
            mountain()
            break
        else:
            break
