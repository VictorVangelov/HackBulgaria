
def count_words(array):
    dic_array = {}
    for word in array:
        if word not in dic_array:
            dic_array[word] = 1
        else:
            dic_array[word] += 1
    return dic_array

