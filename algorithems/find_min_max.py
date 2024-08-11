from array import array


def find_min_value(nums):
    min_value = nums[0]
    min_index = 0

    for index, num in enumerate(nums):
        if num < min_value:
            min_index = index
            min_value = num

    return print(f'min value is: {min_value} and its index is: {min_index}') 


def find_max_value(nums):
    max_value = nums[0]
    max_index = 0

    for index, num in enumerate(nums):
        if num > max_value:
            max_value = num
            max_index = index

    return print(f'max value is: {max_value} and its index is: {max_index}') 


nums = array('i', [ 23, 99, 34, 567, 47, 234, 57, 61, 12, 77, 86, 1, 90])

find_min_value(nums)
find_max_value(nums)