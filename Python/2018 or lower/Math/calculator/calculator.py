# Made by Parker Cranfield
#
#Imports
from time import sleep

#Start
print("Welcome! What do you wanna do?")
print("add")
print("subtract")
print("multiply")
print("divide")
sleep(1)
choice1 = input("Type one of them exactly: ")


#If statements + main function

def main():
    if choice1 == "add":
        add()
    elif choice1 == "subtract":
        subtract()
    elif choice1 == "multiply":
        multiply()
    elif choice1 == "divide":
        divide()
    else :
        print("Error")
        sleep(2)
        main()



#Funtions
def add():
    num = int(input("First number: "))
    num2 = int(input("Seconde number: "))
    print(num + num2)
    wait = input("")

def subtract():
    num = int(input("First number: "))
    num2 = int(input("Seconde number: "))
    print(num - num2)
    wait = input("")

def multiply():
    num = int(input("First number: "))
    num2 = int(input("Seconde number: "))
    print(num * num2)
    wait = input("")

def divide():
    num = int(input("First number: "))
    num2 = int(input("Seconde number: "))
    print(num // num2)
    wait = input("")

if __name__ == main():
    main()
