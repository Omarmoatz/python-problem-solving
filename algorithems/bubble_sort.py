# time complexitiy: O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return print(arr)


arr = [14, 70, 11, 9, 1, 56]

print(bubble_sort(arr))
