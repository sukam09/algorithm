input = __import__('sys').stdin.readline
N, K = map(int, input().split())

def fact(n):
    if n <= 1: return 1
    else:
        val = 1
        for i in range(2, n + 1): val *= i
        return val

print(fact(N) // fact(N - K) // fact(K) % 10007)