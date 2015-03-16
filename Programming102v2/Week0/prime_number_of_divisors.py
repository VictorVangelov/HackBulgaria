from is_prime import is_prime


def prime_number_of_divisors(number):
    num = number
    numbers = []
    while num >= 1:
        if number % num == 0:
            numbers.append(num)
        num = num - 1
    return is_prime(len(numbers))
print (prime_number_of_divisors(7))
