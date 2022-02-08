#   Tip Calculator
#   Coded by: Parker Cranfield
#   May 18, 2019

def main():
    total = int(input("Please input the total: "))
    tipPercentage = int(input("Please put in the tip percentage, without the percent sign: "))

    e = tipPercentage/100
    f = e*total
    newTotal = f + total
    print("New total is " + str(newTotal) + "\n")
    while True:
        again = input("Another? [y/n]: ")
        if again != "y" and again != "n":
            print("Try again")
            continue
        elif again == "y":
            main()
        else:
            exit()

if __name__ == "__main__":
    main()
