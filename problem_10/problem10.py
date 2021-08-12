'''
PROBLEM 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def run():
    maximum = 2000000
    sum = 0
    for x in range(2, maximum):
        check_prime(x)
    for prime in primes:
        sum += prime
    print("Sum of primes: {}".format(sum))


def check_prime(x):
    global primes
    for prime in primes:
        if x % prime == 0:
            return
    primes.append(x)


primes = []


if __name__ == '__main__':
    run()