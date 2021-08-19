'''
PROBLEM 4:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
import math

def check_palindrome(integer):
    str_num = str(integer)
    i = 0
    while 2*i < len(str_num):
        if str_num[i] != str_num[len(str_num) - i - 1]:
            return False
        i += 1
    return True


def run():
    a = 0
    b = 0
    largest_palindrome = 0
    while a < 1000 and b < 1000:
        if a == b:
            a = 0
            b += 1
        else:
            a += 1
        if a*b > largest_palindrome:
            if check_palindrome(a*b):
                largest_palindrome = a*b
    print("The Largest Palindrome is {}".format(largest_palindrome))



if __name__ == '__main__':
    run()