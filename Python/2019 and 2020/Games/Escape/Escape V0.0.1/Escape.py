#   "Escape" -- RPG made in python
#   Coded by Parker Cranfield
#   05/29/2019

# IMPORTS
from escapelib import *
from map import *

# VARIBALES
inventory = []
currentRoom = "your room"

# BODY
# displays current status
def status():
  print("---------------------------")
  print("You are in " + YELLOW + currentRoom + RESET_COLOR)
  print("Inventory : " + BLUE + str(inventory) + RESET_COLOR)
  if "item" in rooms[currentRoom]:
    print("You see a " + BLUE + rooms[currentRoom]["item"] + RESET_COLOR)
  print("---------------------------")
  print()

# gets players commands either moves rooms or gets items
def start():
    commands()
    global currentRoom
    global inventory

    while True:
        status()
        # asks player for input when input field is empty
        move = ""
        while move == "":
            move = input(GREEN + ">> " + RESET_COLOR)
            move = move.lower().split()

            # checks if player can enter room -- checks if player has needed item
            if move[0] == "go":
                if move[1] in rooms[currentRoom]:
                    newCurrRoom = currentRoom
                    currentRoom = rooms[currentRoom][move[1]]
                    if rooms[currentRoom]["needed item"] != None:
                        if len(inventory) != 0:
                            check = False
                            for item in inventory:
                                    if item in rooms[currentRoom]["needed item"]:
                                        currentRoom = currentRoom
                                        check = True
                            if not check:
                                currentRoom = newCurrRoom
                        else:
                            print("you do not have the correct item to go this direction")
                            currentRoom = newCurrRoom
                    else:
                        currentRoom = currentRoom
                else:
                    print("You can\'t go that way!")
                    currentRoom = newCurrRoom

            # gets the item the player wants
            if move[0] == "get" :
                if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
                    inventory += [move[1]]
                    print(move[1] + " got!")
                    del rooms[currentRoom]["item"]
                else:
                    print("Can\'t get " + move[1] + "!")

# startup sequence
def main():
    clear()
    resize()
    typewriter("Please make sure you spell everything correctly and do the commands right\n", 0.05)
    typewriter("or the spelling gods will kill the game.\n", 0.05)
    print("\nby the way, for moving only use ['north', 'east', 'south', 'west']")
    print("thanks and enjoy the game!")
    sleep(4)
    clear()
    typewriter("You are all alone in your house...\n", 0.05)
    typewriter("You only have one simple task...", 0.05)
    sleep(1.5)
    clear()
    banner()
    start()
if __name__ == "__main__":
    main()
