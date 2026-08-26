'''
Example Walkthrough

Let's walk through finding needle = "abc" in haystack = "ababcab".

Initial Setup:

    haystack = "ababcab" (length n = 7)
    needle = "abc" (length m = 3)
    We'll check positions from index 0 to 4 (n - m = 7 - 3 = 4)
'''



def example(needle:str,haystack:str):
    if needle == '':
        print(0)
        return 0

    needle_len = len(needle)
    haystack_len = len(haystack)

    if needle_len > haystack_len:
        print(-1)
        return -1
    positions = haystack_len - needle_len + 1
    for index in range(positions):
        if haystack[index:index + positions] == needle:
            print(index)
            return index

    # FORGOTTEN!!!!! If no matches return -1
    return -1




needle = 'abc'
haystack = 'xxxabc'
example(needle,haystack)

needle = ''
haystack = 'xxxabc'
example(needle,haystack)

needle = 'xxxxxxx'
haystack = 'xxxabc'
example(needle,haystack)