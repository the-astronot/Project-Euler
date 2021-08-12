'''
PROBLEM 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def run():
    a = 0
    b = 1
    c = 2
    found = False
    while not found and c < 1000:
        a += 1
        if a > b:
            a = 1
            if b + 1 < c:
                b += 1
            else:
                b = 1
                c += 1
        if a + b + c == 1000:
            found = check_theorem(a,b,c)
    print("A: {0} B: {1} C: {2} Product: {3}".format(a,b,c,a*b*c))


def check_theorem(a,b,c):
    return a**2 + b**2 == c**2


if __name__ == '__main__':
    run()