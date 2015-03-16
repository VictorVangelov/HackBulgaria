def is_increasing(seq):
    i = 0
    while i < len(seq) - 1 and seq[i] < seq[i + 1]:
        i += 1
    return i == len(seq) - 1


