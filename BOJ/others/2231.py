import sys

def dec_sum(n):
	return n + sum([int(x) for x in str(n)])

n = int(sys.stdin.readline())
ans = False
for i in range(1000000):
	if dec_sum(i) == n:
		ans = True
		print(i)
		break
if not ans:
	print(0)