# Binary Search: we will asume that we will search about a number in list of numbers
#                   - Time complexity = log2 n  --> O(log2 n)
#                   - the list must be sorted
from array import array


nums = array('i', [ 23, 99, 34, 567, 47, 234, 57, 61, 12, 77, 86, 90])

def binary_search(nums, value):
    # Convert array to a list, sort it, and convert back to an array
    sorted_nums = array(nums.typecode, sorted(nums))
    # nums.sort()
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((start + end) / 2)

        if sorted_nums[mid] == value:
            print(sorted_nums)
            return f'found it at {mid} with value {sorted_nums[mid]}'
        
        elif sorted_nums[mid] < value:
            start = mid + 1

        else: 
            end = mid - 1



print(binary_search(nums, 567))