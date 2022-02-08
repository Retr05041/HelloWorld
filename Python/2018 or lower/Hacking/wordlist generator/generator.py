# Made by Parker Cranfield
import string
from itertools import product

#=====================================================

f = open("wl1.txt", "w")


def allwords(chars, length):
    for letters in product(chars, repeat=length):
        yield ''.join(letters)

def main():
    letters = string.ascii_lowercase
    for wordlen in range(1, 6):
        for word in allwords(letters, wordlen):
            f.write(word + "\n")

if __name__=="__main__":
    main()

#====================================================


#Make sure to have a file named "wl.txt" in the same folder.... if not make one or chnage the "wl.txt" in the code to a different .txt file
