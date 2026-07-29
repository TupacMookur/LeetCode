'''

An ugly number is a positive integer whose only prime factors are 2, 3, and 5, with 1 included by convention.
The sequence begins as 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, and so on. Given an integer n, return the nth ugly number.

Given an integer n, return true if n is an ugly number.
'''

def example(n):
    # is n a negative number or zero?
    if n <= 0:
        print (False)

    for p in [2,3,5]:
        while n % p == 0:
            n //= p

    # if n is a prime number, this returns a BOOL
    print (n == 1)



example(11)
example(15)