def find_smallest_number(arr):
    if not arr:  
        return None  
    smallest = arr[0]  
    for num in arr:
        if num < smallest:
            smallest = num  
    return smallest


array = [3, 5, 7, 2, 8, -1, 4, 10, 12]
print("The smallest number in the array is:", find_smallest_number(array))
