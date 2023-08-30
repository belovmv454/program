primes = list(range(3, 10 ** 7 + 1, 2))
for i in range(len(primes)- 1):
    for j in range(len(primes) - 1):
        if primes[j] != primes[i] and primes[j] % primes[i] == 0:
            del primes[j]
print(primes)

