def selection_sort(arr):
    n = len(arr)
    for i in range(n):
       
        min_idx = i
    
        for j in range(i+1, n):
           
            if arr[j] < arr[min_idx]:
                min_idx = j
       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [200,60,300,10,700]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
