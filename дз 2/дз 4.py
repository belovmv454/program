primes = [1, 2, 3]
for i in range(4, int((10 ** 7) ** 0.5)):
    c = 0
    if i > (10 ** 7) ** 0.5:
        break
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                c += 1
        if c == i - 2:
            primes.append(i)
print(primes)
        
