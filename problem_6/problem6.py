'''
PROBLEM 6:

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def run():
    max_number = 100
    difference = (get_square_of_sums(max_number) -
                 get_sum_of_squares(max_number))
    
    print("The Difference is {}".format(difference))

def get_sum_of_squares(max_num):
    sum = 0
    for x in range(max_num+1):
        sum += x**2
    return sum

def get_square_of_sums(max_num):
    sum = 0
    for x in range(max_num+1):
        sum += x
    return sum**2


if __name__ == '__main__':
    run()