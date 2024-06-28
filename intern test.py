from collections import Counter

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Count the frequency of elements in both arrays
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    print(count_arr)
    print(count_brr[202])

    
    missing = []
    
    # Compare frequencies in brr to arr
    for num in count_brr:
        if count_brr[num] > count_arr[num]:
            missing.append(num)
    
    # Return the sorted list of missing numbers
    return sorted(missing)

print(missingNumbers([1,2,3,4],[1,202,3,4,5,6,4]))