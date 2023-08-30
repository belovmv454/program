def similarwords(A, B):
    c = ''
    for i in range(5):
        if A[i] == B[i]:
            c += '+'
        elif A[i] in B:
            c += '.'
        else:
            c += '-'
    return c
assert(similarwords('кошка','полка')) == '.+-++'
assert(similarwords('абаба','бабаб')) == '.....'
assert(similarwords('полка','полка')) == '+++++'
assert(similarwords('гараж','полки')) == '-----'
assert(similarwords('баббб','ааббб')) == '.++++'

#всего можеь быть 3 ** 5 разныч ответов#
