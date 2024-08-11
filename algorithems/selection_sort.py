
def selection_sort(arr):
    for num in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = num

        for n in range(num+1, len(arr)):
            if arr[n] < arr[min_index]:
                min_index = n
        # Swap the found minimum element with the first element
        arr[num], arr[min_index] = arr[min_index] , arr[num]

    return print(arr)

arr = [14, 70, 11, 9, 1, 56]

print(selection_sort(arr))
        
    
