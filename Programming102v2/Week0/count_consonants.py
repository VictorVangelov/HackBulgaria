def consonants(str):
    consonants = 'bcdfghjklmnpqrstvwxz'
    all_consonants = consonants + consonants.upper()
    return count_of_letters(str, all_consonants)


def count_of_letters(string, letters):
    return sum(map(lambda letter: string.count(letter), letters))
