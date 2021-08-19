'''
PROBLEM 23:

A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.

'''
import math

def run():
    maximum = 30000
    abundant_nums = []
    numbers = [0 for _ in range(maximum+1)]
    sum = 0
    for x in range(1, maximum):
        if sum_divisors(x) > x:
            abundant_nums.append(x)
    a = 0
    b = 0
    while b < len(abundant_nums):
        if abundant_nums[a] + abundant_nums[b] < len(numbers):
            numbers[abundant_nums[a]+abundant_nums[b]] = 1
        if a+1 < len(abundant_nums):
            a += 1
        else:
            b += 1
            a = b
    
    for x in range(1,len(numbers)):
        if numbers[x] == 0:
            sum += x

    print("The sum of the numbers which are not the sum of "\
            + "abundant numbers is: {}".format(sum))
    #print(numbers)
        

def sum_divisors(num):
    sum = 0
    for x in range(1, math.ceil(math.sqrt(num))):
        if num % x == 0:
            sum += x
            if num/x != x and num/x != num:
                sum += num/x
    return sum


if __name__ == '__main__':
    run()
