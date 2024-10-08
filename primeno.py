def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(num**0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if num % divisor == 0:
            return False
    return True


number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
