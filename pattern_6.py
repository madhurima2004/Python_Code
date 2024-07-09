def inverted_pyramid_pattern(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

n = 5
inverted_pyramid_pattern(n)
