def sevens_in_a_row(array, num):
    return num <= len(list(filter(lambda x: x == 7, array)))
print (sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
