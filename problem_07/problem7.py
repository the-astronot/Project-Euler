'''
PROBLEM 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def run():
    global primes
    x = 2
    while len(primes) < 10001:
        check_prime(x)
        x+=1
    print("The 10001st Prime is {}".format(primes[10000]))


def check_prime(number):
    global primes
    for y in primes:
        if number % y == 0:
            return
    primes.append(number)


primes = []


if __name__ == '__main__':
    run()