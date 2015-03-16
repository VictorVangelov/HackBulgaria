def count_vowels(str):
    vowels = 'ioaeyu'
    all_vowels = vowels + vowels.upper()
    return count_of_letters(str, all_vowels)


def count_of_letters(string, letters):
    return sum(map(lambda letter: string.count(letter), letters))
