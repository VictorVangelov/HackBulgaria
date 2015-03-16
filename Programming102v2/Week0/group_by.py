def group_by(func, seq):
    result = {}

    for item in seq:
        key = func(item)

        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result
