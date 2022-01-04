def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
primes = [i for i in range(2, 104) if prime(i)]

for i in range(len(primes) - 1):
    special_num = primes[i] * primes[i + 1]
    if special_num > n:
        print(special_num)
        break