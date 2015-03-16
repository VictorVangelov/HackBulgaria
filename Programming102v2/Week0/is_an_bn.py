def is_an_bn(word):
    print(len(word))
    if word == "":
        return False
    elif len(word) % 2 == 0:
        last_index = int(len(word) / 2)
        for char in range(0, last_index):
            if not (word[char] == 'a' and word[len(word) - 1 - char] == 'b'):
                print("first mistake is in position ", char)
                return False
        return True
    else:
        return False

print (is_an_bn("aaaaabbbbb"))
