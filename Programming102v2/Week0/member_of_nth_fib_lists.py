from nth_fib_lists import nth_fib_lists


def lists_are_equal(listA, listB):
    if not(len(listA) == len(listB)):
        return False
    else:
        for i in range(len(listA)):
            if listA[i] != listB[i]:
                return False
    return True


def member_of_nth_fib_lists(listA, listB, needle):
    n = 1
    fib_lists = nth_fib_lists(listA, listB, n)
    while len(fib_lists) <= len(needle):
        if lists_are_equal(fib_lists, needle):
            return True
        n += 1
        fib_lists = nth_fib_lists(listA, listB, n)
    return False

#print (member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
