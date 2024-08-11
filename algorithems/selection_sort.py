# time complexitiy: O(n^2)
def selection_sort(arr):
    for num in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        for n in range(num+1, len(arr)):
            if arr[n] < arr[num]:
                # Swap the found minimum element with the first element
                arr[num], arr[n] = arr[n] , arr[num]
        
        

    return print(arr)


arr = [14, 70, 11, 9, 1, 56]

print(selection_sort(arr))
        
    
