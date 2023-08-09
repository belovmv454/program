def matriza(L):
    for i in reversed(range(1, len(L[0]))):
        c = 0
        for j in range(len(L)):
            if L[j][i] > 0:
                c += 1
            else:
                break
        if c == len(L):
            for j in range(len(L)):
                r = L[j][0]
                L[j][0] = L[j][i]
                L[j][i] = r
            return L
    return L
assert(reversed([[1, 2],[3, 4],[5, 6]])) == [[2, 1],[4, 3],[6, 5]]
