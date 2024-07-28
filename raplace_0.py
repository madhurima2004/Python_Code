def replace_zeros_in_list(numbers):
    return [1 if x == 0 else x for x in numbers]

numbers = [0, 4, 0, 5, 2, 0, 9, 0]
new_numbers = replace_zeros_in_list(numbers)
print(new_numbers)
