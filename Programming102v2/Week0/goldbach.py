from is_prime import is_prime


def prime_numbers_of_divisors(number):
    num = number
    numbers = []
    while num >= 1:
        if is_prime(num):
            numbers.append(num)
        num = num - 1
    return (list(sorted(numbers)))


def goldbach(num):
    result = []
    for prime in prime_numbers_of_divisors(num):
        if is_prime(num - prime):
            result.append((prime, num - prime))

    return result
