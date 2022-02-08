# --<{     Number letter counts     }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{       August 24, 2020        }>--

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def transform(n):
    lst = []
    ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens = {10: "ten", 11:"eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3:"thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    hundreds  = {1:"one hundred", 2: "two hundred", 3:"three hundred", 4: "four hundred", 5: "five hundred", 6: "six hundred", 7: "seven hundred", 8: "eight hundred", 9: "nine hundred"}
    n = str(n)
    for char in n:
        lst.append(char)
    if len(lst) > 1:
        if len(lst) > 2:
            if len(lst) > 3:
                new_str = "one thousand"
            else:
                if int(lst[1]) == 0 and int(lst[2]) == 0:
                        new_str = hundreds[int(lst[0])]
                elif int(lst[1]) != 0 and int(lst[2]) == 0:
                    if int(lst[1]) < 2:
                        temp = lst[0]
                        lst.remove(lst[0])
                        lst = "".join(lst)
                        new_str = hundreds[int(temp)] + " and " + teens[int(lst)]
                    else:
                        temp = lst[0]
                        lst.remove(lst[2])
                        lst.remove(lst[0])
                        lst = "".join(lst)
                        new_str = hundreds[int(temp)] + " and " + tens[int(lst)]
                elif int(lst[1]) == 0 and int(lst[2]) != 0:
                    if int(lst[1]) < 2:
                        temp = lst[0]
                        lst.remove(lst[0])
                        lst = "".join(lst)
                        new_str = hundreds[int(temp)] + " and " + ones[int(lst)]
                else:
                    if int(lst[1]) < 2:
                        temp = lst[0]
                        lst.remove(lst[0])
                        lst = "".join(lst)
                        new_str = hundreds[int(temp)] + " and " + teens[int(lst)]
                    else:
                        new_str = hundreds[int(lst[0])] + " and " + tens[int(lst[1])] + " " + ones[int(lst[2])]
        else:
            if int(lst[0]) < 2:
                lst = "".join(lst)
                new_str = teens[int(lst)]
            else:
                if int(lst[1]) == 0:
                    new_str = tens[int(lst[0])]
                else:
                    new_str = tens[int(lst[0])] + " " + ones[int(lst[1])]
    else:
        new_str = ones[int(lst[0])]

    return new_str




if __name__ == "__main__":
    word_lst = []
    total = 0
    counter = 0
    for i in range(1, 1001):
        word_lst.append(transform(i))
    word_lst = [" ".join(word_lst)]
    for word in word_lst:
        temp = word
    add_lst = temp.split()
    for n in add_lst:
        total += counter
        counter = 0
        for char in n:
            counter += 1
            print(f"{char} | {counter} | {total}", end="\r", flush=True)
    total += counter
    print("\r")
    print(total)