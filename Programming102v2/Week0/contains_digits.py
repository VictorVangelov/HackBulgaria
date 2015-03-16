from contains_digit import contains_digit


def contains_digits(number, digits):
    contained = list(filter(lambda x: contains_digit(number, x), digits))
    return len(digits) == len(contained)
print(contains_digits(402123, [0, 3, 4]))
