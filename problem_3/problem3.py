'''
PROBLEM 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import math


def run():
	global primes
	maximum = 600851475143
	largest_prime_factor = None
	for x in range(2, math.ceil(math.sqrt(maximum))):
		is_prime = True
		for prime in primes:
				if x % prime == 0:
					is_prime = False
					break
		if is_prime:
			primes.append(x)
			if maximum % x == 0:
				largest_prime_factor = x
	print("Largest Prime Factor: {}".format(largest_prime_factor))
		

primes = []


if __name__ == '__main__':
	run()
