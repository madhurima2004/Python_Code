def pyramid_character_pattern(n):
    num = 65  # ASCII value for 'A'
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print(chr(num), end="")
        print()


pyramid_character_pattern(5)
