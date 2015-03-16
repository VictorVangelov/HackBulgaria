#solution 1
def count_substrings(haystack, needle):
    start = haystack.find(needle)
    count = -1
    if start != -1:
        count = count + 1
        while start != -1:
            count += 1
            start += len(needle)
            start = haystack.find(needle, start)
    else:
        count = 0
    return count

#solution 2
#def count_substrings(haystack, needle):
#    return haystack.count(needle)
