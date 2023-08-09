def revers(L, k):
        if len(L) == 1:
            k.append(L[0])
            print(k)
        else:
            k.append(L[-1])
            del L[-1]
            revers(L, k)
print(revers([1, 2, 3, 4, 5], []))
print(revers([1], []))
#программа выводит ответ и почему то после этого еще и "None", поэтому проверил через print
