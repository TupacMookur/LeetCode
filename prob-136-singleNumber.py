### REDUCE XOR !!!!!!!!!!!!!!!!!!!!!!

from typing import List
from functools import reduce
from operator import xor

#    a XOR a = 0
#    a XOR 0 = a

'''functools.reduce applies a binary function cumulatively to the items in an iterable (left to right) until the iterable becomes a single value. It’s part of the functools module and can take an optional initializer as the starting value.'''



print(7 ^ 0)
print(7 ^ 7)



def example(nums):
    print(reduce(xor,nums))

nums = [2,1,2,1,5]

example(nums)





'''
Problem Description

You are given a non-empty array of integers called nums. In this array, every element appears exactly twice except for one element that appears only once. Your task is to find and return that single element.

The challenge comes with two important constraints:

    Your solution must run in linear time complexity, meaning O(n) where n is the number of elements in the array
    You must use only constant extra space, meaning O(1) space complexity

For example:

    If nums = [2, 2, 1], the answer would be 1 since it's the only number that appears once
    If nums = [4, 1, 2, 1, 2], the answer would be 4 since all other numbers appear twice

The solution leverages the XOR bitwise operation, which has special properties that make it perfect for this problem. When you XOR a number with itself, the result is 0 (x ^ x = 0), and when you XOR any number with 0, you get the original number back (x ^ 0 = x). By XORing all numbers in the array together, the duplicate pairs cancel each other out (become 0), leaving only the single number that appears once.


This is where XOR becomes the perfect tool. XOR has a beautiful mathematical property: a ^ a = 0 for any number a. This means when we encounter the same number twice, they neutralize each other. Additionally, 0 ^ b = b, meaning that XORing with 0 doesn't change the number.




Example Walkthrough

Let's walk through a small example with nums = [5, 3, 5] to see how the XOR approach finds the single number.

Step-by-step XOR operations:

    Start with the first element: result = 5
    XOR with the second element: result = 5 ^ 3
        In binary: 101 ^ 011 = 110 (which is 6 in decimal)
    XOR with the third element: result = 6 ^ 5
        In binary: 110 ^ 101 = 011 (which is 3 in decimal)

Why this works: Due to XOR's commutative property, we can rearrange the operations:

    5 ^ 3 ^ 5 = 5 ^ 5 ^ 3 = (5 ^ 5) ^ 3 = 0 ^ 3 = 3

The two 5's cancel each other out (since 5 ^ 5 = 0), leaving us with 3, which is indeed the single number that appears only once.

Another example with more numbers: nums = [7, 2, 7, 9, 2]

Processing in order:

    result = 7
    result = 7 ^ 2 = 5
    result = 5 ^ 7 = 2
    result = 2 ^ 9 = 11
    result = 11 ^ 2 = 9

Conceptually regrouping: (7 ^ 7) ^ (2 ^ 2) ^ 9 = 0 ^ 0 ^ 9 = 9

The duplicate pairs (7,7) and (2,2) both XOR to 0, and since 0 ^ 9 = 9, we're left with 9 as our answer. This demonstrates how XOR naturally filters out all paired elements while preserving the single unique element.


'''
