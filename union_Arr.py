def union_of_arrays(array1, array2):

    set1 = set(array1)
    set2 = set(array2)
    

    union_set = set1.union(set2)
    
    union_list = list(union_set)
    
    return union_list


array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

result = union_of_arrays(array1, array2)
print("Union of arrays:", result)
