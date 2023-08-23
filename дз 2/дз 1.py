def matriza(L):
    final = []
    r1 = len(L[0]) - 1
    r2 = 0
    f = 0
    for j in range(len(L[0]) - 1):
        summa = 0
        r1 -= 1
        f += 1
        for i in range(f + 1):
            summa += L[r1 + i][r2 + i]
        final.append(summa)
    r1 = 0
    r2 = len(L[0]) - 1
    f = 0
    for i in range(len(L[0]) - 2):
        summa = 0
        r2 -= 1
        f += 1
        for j in range(f + 1):
            summa += L[r1 + j][r2 + j]
        final.append(summa)
    return final
assert(matriza([[1, 8],[4, 9]])) == [10]
assert(matriza([[6, 9, 7],[4, 6, 7], [9, 0, 5]])) == [4, 17, 16]
assert(matriza([[1, 6, 8],[4, 1, 7], [8, 9, 5]])) == [13, 7, 13]
assert(matriza([[1, 2, 3, 4],[5, 6, 7, 8], [4, 3, 2, 1], [8, 7, 6, 5]])) == [11, 14, 14, 11, 10]

