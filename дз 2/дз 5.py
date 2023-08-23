def del1(a, b):
    final = []
    for i in range(a, b + 1):
        if (i ** 0.5) ** 0.5 == int((i ** 0.5) ** 0.5):
            c = 0
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0 and j != i ** 0.5:
                    c += 2
                    
                elif j == i ** 0.5:
                    c += 1
            if c == 5:
                final.append(i)
    return final

        
        
