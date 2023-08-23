def abc(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "x любое число"
    elif a == 0 and b == 0 and c != 0:
        return 'нет решений'
    elif a == 0 and c != 0 and b != 0:
        x1 = -c / b
        return x1
    elif a == 0 and c == 0 and b != 0:
        return 0
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return 'нет решений'
        else:
            x1 = ((-b) + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            return x1, x2
assert(abc(1, -5, 9)) == 'нет решений'
assert(abc(0, 8, 0)) == 0
assert(abc(0, 3, -9)) == 3
assert(abc(-3, 0, 75)) == (-5.0, 5.0)
assert(abc(5, 0, 0)) == (0, 0)
assert(abc(0, 0, 0)) == 'x любое число'
assert(abc(0, 0, 9)) == 'нет решений'
print(abc(7, 0, -14))
assert(abc(7, 0, -14)) == (2 ** 0.5, -2 ** 0.5)
assert(abc(1, -12, 36)) == (6, 6)
