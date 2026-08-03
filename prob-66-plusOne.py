'''

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

'''

def example(digits):

    n = len(digits)
    print(f'{n} digits')


    # Iterate through digits from right to left (least significant to most significant)

    # start, move left, stop
    for i in range(n - 1, -1, -1):
        # Add 1 to the current digit
        print(f'{digits[i]} is the value of index {i} before +1')
        digits[i] += 1
        print(f'{digits[i]} is the value of index {i} after +1\n')
        # Handle carry by taking modulo 10
        digits[i] %= 10
        print(f'{digits[i]} is the value of index {i} after modulo 10\n')

        # If the digit is not 0, there's no carry, so we can return
        if digits[i] != 0:
            print(digits)
            return digits


    # If we reach here, all digits were 9 (e.g., 999 -> 1000)
    # Need to add a leading 1
    print ([1] + digits)


list = [9,9,9]
example(list)