'''
class Solution:
    def maxProduct(self, n: int) -> int:
        # Initialize variables to track the two largest digits

        digits = sorted(int(d) for d in str(n))
        return digits[1] * digits[-1]
'''



def example(n):
    a = b = 0
    while n:
        # divmod returns a tuple

        n, x = divmod(n, 10)
        if a < x:
            a, b = x, a

        elif b < x:
            a, b = a, x

    print(a * b)


example(2345789)

'''
SUBMITTED ANSWER BELOW
'''



class Solution:
    def maxProduct(self, n: int) -> int:

        a = b = 0
        while n:
            n, x = divmod(n, 10)
            if x > a:
                a, b = x, a

            elif x > b:
                a, b = a, x
        return a * b


