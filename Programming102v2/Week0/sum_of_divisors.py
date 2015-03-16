def sum_of_divisors(n):
    sum = 0
    count = n
    while count >= 1:
        if n % count == 0:
            sum += count
        count -= 1
    return sum
print (sum_of_divisors(8))
