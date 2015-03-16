def simplify_fraction(fraction):
    nominator, denumenator = fraction
    nod = find_nod(nominator, denumenator)
    return (nominator / nod, denumenator / nod)


def find_nod(a, b):
    if a - b == 0:
        return a
    else:
        find_nod(abs(a - b), min(a, b))
