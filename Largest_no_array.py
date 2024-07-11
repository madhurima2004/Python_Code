def find_largest_number(arr):
    if not arr:  
        return None  
    largest = arr[0]  
    for num in arr:
        if num > largest:
            largest = num  
    return largest


array = [3, 5, 7, 2, 8, -1, 4, 10, 12]
print("The largest number in the array is:", find_largest_number(array))
