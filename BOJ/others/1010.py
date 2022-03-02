def fact(n):
	if n <= 1: return 1
	else:
		res = 1
		for i in range(2, n + 1): res *= i
		return res

input = __import__('sys').stdin.readline
T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	print(fact(M) // fact(M - N) // fact(N))