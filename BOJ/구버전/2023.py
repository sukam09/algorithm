from math import sqrt

def sieve(N):
    prime['0'], prime['1'] = False, False
    for i in range(2, int(sqrt(10 ** N)) + 1):
        if prime[str(i)]:
            for j in range(i * 2, 10 ** N, i):
                prime[str(j)] = False

N = int(input())
prime = {str(i): True for i in range(10 ** N)}
sieve(N)
ans = ['2', '3', '5', '7']
for i in range(1, N):
    res = []
    for p in ans:
        for j in range(10):
            j = str(j)
            if prime[p + j]:
                res.append(p + j)
    ans = res
for p in ans:
    print(p)