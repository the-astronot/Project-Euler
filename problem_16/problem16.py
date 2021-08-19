'''
PROBLEM 16:

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''


def run():
    number = 2**1000
    str_num = str(number)
    sum = 0
    for number in str_num:
        sum += int(number)
    print("The sum of the digits is: {}".format(sum))


if __name__ == '__main__':
    run()
