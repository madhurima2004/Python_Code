def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


arr = [3, 60, 80, 10, 100, 2, 150]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
