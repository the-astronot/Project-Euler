'''
PROBLEM 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def run():
    smallest_number = 1
    for x in range(20):
        while not check_recursive(smallest_number, x+1):
            smallest_number += x
    print("Smallest Number Divisible By All is {}".format(smallest_number))


def check_recursive(number, divisor):
    if divisor != 0:
        if number % divisor == 0:
            return check_recursive(number, divisor-1)
        return False
    return True



if __name__ == '__main__':
    run()