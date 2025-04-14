def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

for odometer in range(1000000):
    if is_palindrome(odometer % 100000) and is_palindrome((odometer + 1) % 100000):
        if is_palindrome((odometer + 2) % 1000000) and is_palindrome((odometer + 3)):
            print(odometer)
            break
