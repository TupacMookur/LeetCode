# return index of 2 numbers that add up to target
from typing import List

def example(nums: List[int], target:int):

    # Dictionary/Hashmap to store number -> index mapping
    num_to_index = {}

    # Iterate through the array with index and value
    for index, num in enumerate(nums):

        # Calculate the complement needed to reach target
        complement = target - num

        # Check if complement exists in our dictionary <------------
        if complement in num_to_index:
            # Found the pair! Return indices
            print(f'Success! Use index {[num_to_index[complement], index]}')

            return [num_to_index[complement], index]

        # Store current number and its index for future lookups
        num_to_index[num] = index
        print(num_to_index)


nums = [1,2,3,4,12]
example(nums,16)

nums = [1,2,3,4,5,6]
example(nums,10)