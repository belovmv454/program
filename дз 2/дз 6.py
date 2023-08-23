def chess(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        ladya = 'Yes'
    else:
        ladya = 'No'
    if abs(x1 - x2) == abs(y1 - y2):
        slon = 'Yes'
    else:
        slon = 'No'
    if slon == 'Yes' or ladya == 'Yes':
        ferz = 'Yes'
    else:
        ferz = 'No'
    if (abs(x1 - x2) == 1 or abs(x1 - x2) == 0) and (abs(y1 - y2) == 1 or abs(y1 - y2) == 0):
        king = 'Yes'
    else:
        king = 'No'
    if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
        kon = 'Yes'
    else:
        kon = 'No'
    return kon, slon, ladya, ferz, king
assert(chess(4, 3, 5, 5)) == ('Yes', 'No', 'No', 'No', 'No')
assert(chess(2, 5, 6, 5)) == ('No', 'No', 'Yes', 'Yes', 'No')
assert(chess(6, 7, 5, 6)) == ('No', 'Yes', 'No', 'Yes', 'Yes')
assert(chess(4, 6, 1, 3)) == ('No', 'Yes', 'No', 'Yes', 'No')
assert(chess(2, 6, 6, 5)) ==('No', 'No', 'No', 'No', 'No')
