# Made by Parker Cranfield
def computer_guess(num):
    low = 1
    high = 10000000000000000000000000000000000000000000000000000000000000000000
    guess = high/2
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")


def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 10000000000000000000000000000000000000000000000000000000000000000000:
        print("Must be in range [1, 10000000000000000000000000000000000000000000000000000000000000000000]")
    else:
        computer_guess(num)

if __name__ == '__main__':
    main()
