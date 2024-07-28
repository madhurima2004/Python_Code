def print_hollow_box(width, height):
    for i in range(height):
        for j in range(width):
           
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print() 

# Example usage
print_hollow_box(10, 5)
