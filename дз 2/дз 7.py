def numbers6(n):
    c = 0
    n = str(n)
    for i in range(1, len(n) + 1):
        for j in range(len(n) + 1 - i):
            if  int(n[j:j + i]) == 0:
                c += 1
            elif int(n[j:j + i][0]) != 0 and int(n[j:j + i]) % 6 == 0:
                c += 1
    return c
assert(numbers6(606)) == 5
assert(numbers6(4806)) == 5
assert(numbers6(0)) == 1
assert(numbers6(1775)) == 0
assert(numbers6(106)) == 2
