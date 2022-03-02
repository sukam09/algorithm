import sys
import math

n_list = []
prime = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        n_list.append(n)

prime_min, prime_max = min(n_list), max(n_list)

# Sieve of Eratosthenes
e = {x: 1 for x in range(2, 2 * prime_max + 1)}
while True:
    p = list(e.keys())[0]
    prime.append(p)
    del e[p]
    if p <= math.sqrt(2 * prime_max):
        keys = list(e.keys())
        for key in keys:
            if key % p == 0:
                del e[key]
    else:
        prime.extend([x for x in e])
        break

for n in n_list:
    ans = [x for x in prime if x > n if x <= 2 * n]
    print(len(ans))