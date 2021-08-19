'''
PROBLEM 21:

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


def run():
    maximum = 10000
    sum = 0
    amicable_nums = []
    pair_dict = dict()
    for x in range(1, maximum):
        amicable_sum = 0
        for y in range(1, x):
            if x % y == 0:
                amicable_sum += y
        if amicable_sum != x:
            if amicable_sum in pair_dict:
                pair_dict[amicable_sum].append(x)
            else:
                pair_dict[amicable_sum] = [x]
    for key in pair_dict:
        for value in pair_dict[key]:
            if value in pair_dict:
                for new_key in pair_dict[value]:
                    if key == new_key:
                        amicable_nums.append(key)
    for num in amicable_nums:
        sum += num
    print("The sum of the amicable numbers is: {}".format(sum))



if __name__ == '__main__':
    run()
