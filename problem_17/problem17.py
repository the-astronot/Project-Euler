'''
PROBLEM 17:

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. The use of "and" when 
writing out numbers is in compliance with British usage.

'''


def run():
    sum = 0
    for x in range(1,1001):
        sum += deconstruct(x)
    print(sum)


def deconstruct(x):
    phrase = ""
    length = len(str(x))
    str_x = str(x)
    if len(str_x) > 1 and str_x[length-2] == "1":
        for y in range(length-2):
            phrase += number[length-y][int(str_x[y])]
            if (x % 10**(length-y)) != 0:
                phrase += magnitude[length-y]
            if length-y == 3:
                if x%100 != 0:
                    phrase += "and"
        phrase += special[int(str_x[-1])]
    else:
        for y in range(length):
            phrase += number[length-y][int(str_x[y])]
            if (x % 10**(length-y)) != 0:
                phrase += magnitude[length-y]
            if length-y == 3:
                if x%100 != 0:
                    phrase += "and"
    print(phrase)
    return len(phrase)


ones = ["","one", "two", "three", "four", "five", "six", "seven", \
        "eight", "nine"]
tens = ["","ten", "twenty", "thirty", "forty", "fifty", "sixty", \
        "seventy", "eighty", "ninety"]
number = ["",ones, tens, ones, ones]
magnitude = ["","","","hundred", "thousand"]
special = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen",\
           "sixteen", "seventeen", "eighteen", "nineteen"]

if __name__ == '__main__':
    run()
