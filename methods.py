def powers(x, y):
    if y < 0:
        return (1 / x) * powers(x, y + 1)
    elif y == 0:
        return 1
    else:
        if y == 1:
            return x
        else:
            return x * powers(x, y - 1)


def cat_ears(n):
    if n % 1 == 0:
        if n < 0:
            return -2
        elif n == 0:
            return 0
        elif n == 1:
            return 2
        else:
            return 2 + cat_ears(n - 1)
    else:
        return -1


def alien_ears(n):
    if n < 0:
        return -2
    elif n % 1 == 0:
        if n == 0:
            return 0
        elif n % 2 == 0:
            return 3 + alien_ears(n - 1)
        else:
            return 2 + alien_ears(n - 1)
    else:
        return -1
