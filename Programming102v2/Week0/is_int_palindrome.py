def is_int_palindrome(n):
    num = str(n)
    for n in range(0, int(len(str(num)) / 2) + 1):
        if num[n] == num[len(num) - 1 - n]:
            return True
    return False
print(is_int_palindrome(121))
