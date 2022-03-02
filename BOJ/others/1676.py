input = __import__('sys').stdin.readline

def fact(n):
	if n <= 1: return 1
	else:
		res = 1
		for i in range(2, n + 1): res *= i
		return res

N = int(input())
cnt = 0
for c in str(fact(N))[::-1]:
	if c != '0':
		print(cnt)
		break
	else: cnt += 1