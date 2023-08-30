primes = [2, 3, 5, 7]
for i in range(9, int((10 ** 7) ** 0.5), 2):
    c = 0
    if i > (10 ** 7) ** 0.5:
        break
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
            else:
                c += 1
        if c == int(i ** 0.5) + 1 - 2:
            primes.append(i)
print(primes)
        
