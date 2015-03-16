def prepare_meal(num):
    word = ''
    if num == 5:
        word = 'eggs'
        return word
    else:
        while (num % 3 == 0 or num % 5 == 0):
            if num % 3 == 0:
                word += ('spam ')
                num = num / 3
            elif num % 5 == 0:
                word += ('and eggs')
                num = num / 5
    return word
