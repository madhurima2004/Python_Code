def is_palindrome(s):

    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

test_string = "A man, a plan, a canal, Panama!"
print(f'Is "{test_string}" a palindrome? {is_palindrome(test_string)}')
