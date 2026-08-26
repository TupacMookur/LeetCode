### BINARY SEARCH !!!!!!!!!!!!!!!!!!!!!!!!!


"""
Find the integer square root using the binary search template.
Finds the first value where mid * mid > x, then returns mid - 1.
"""

def example(x):
    value = x
    x = x ** .5
    print(f'the sqrt of {value} is {x}')

#example(9)


# the above CANNOT be used for this problem
#======================================================================================================================
def algoMonster(x:int):
        if x == 0:
            print(0)
            return 0
#======================================================================================================================



        index = -1
        left, right = 1, x
        middle = 0
        while left <= right:    #  1 <= 8
            print(left,right)

            middle = (left + right) // 2   # 4
            print(f'{left} + {right} // 2 is {middle}')
            print(f'middle is {middle}')
            answer = x // middle
            print(f'           x which is {x} divided by {middle} is {answer}')

            if middle > x // middle:     # 4     if middle is MORE than half of X subtract 1 from the right side
                # set the index here
                index = middle
                right = middle - 1
                print(f'middle is {middle}')
                print(f'right = middle -1 which is {right}')
            else:                       #         middle is NOT greater than x // middle add 1 to the LEFT slider
                left = middle + 1
                print(f'left is now {left}')
        if index == -1:
            return x
        print(index -1)
        return index -1






algoMonster(8)     # answer is 2