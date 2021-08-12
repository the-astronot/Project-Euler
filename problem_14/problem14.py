'''
PROBLEM 14:

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''


def run():
    longest_chain = 0
    best_starting_point = 0
    maximum = 1000000
    for i in range(1,maximum):
        chain = collatz(i)
        if chain > longest_chain:
            longest_chain = chain
            best_starting_point = i
    print("The Longest Chain Starts with: {}".format(best_starting_point))


def collatz(starting_point):
    num_steps = 0
    x = starting_point
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        num_steps += 1
    return num_steps


if __name__ == '__main__':
    run()
