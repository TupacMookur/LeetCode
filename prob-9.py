'''
Palendrome?   True or False
'''

def example(x):
    # Negative numbers aren't palindromes
    if (x < 0 or
            # Zero is a palindrome
            # The last digit cannot be a ZERO <-----------------------
            (x != 0 and x % 10 == 0)):
        print(False)

    reversed_half = 0
    while reversed_half < x:
        # take reverse half, move decimal place over, and add the next digit to the reversed half
        reversed_half = (reversed_half * 10) + (x % 10)
        print(reversed_half)

        # reassign X with one less digit
        x //= 10

    #return x == reversed_half or x == reversed_half // 10
    print (x == reversed_half or x == reversed_half // 10)


example(1234321)




'''
Step 2: Reverse the Second Half

We start with x = 12321 and y = 0. Now we'll extract digits from the end of x and build y:

    Iteration 1:
        Extract last digit: 12321 % 10 = 1
        Build reversed number: y = 0 * 10 + 1 = 1
        Remove last digit from x: x = 12321 // 10 = 1232
        Check condition: y = 1 < x = 1232, continue

    Iteration 2:
        Extract last digit: 1232 % 10 = 2
        Build reversed number: y = 1 * 10 + 2 = 12
        Remove last digit from x: x = 1232 // 10 = 123
        Check condition: y = 12 < x = 123, continue

    Iteration 3:
        Extract last digit: 123 % 10 = 3
        Build reversed number: y = 12 * 10 + 3 = 123
        Remove last digit from x: x = 123 // 10 = 12
        Check condition: y = 123 >= x = 12, stop
'''