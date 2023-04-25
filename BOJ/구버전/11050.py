import sys

def fact(n):
	return n * fact(n - 1) if n > 0 else 1

N, K = map(int, sys.stdin.readline().split())
print(fact(N) // (fact(N - K) * fact(K)))