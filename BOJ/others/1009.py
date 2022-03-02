import sys

T = int(sys.stdin.readline())
digit = {}
digit[2] = [2, 4, 8, 6]
digit[3] = [3, 9, 7, 1]
digit[4] = [4, 6]
digit[7] = [7, 9, 3, 1]
digit[8] = [8, 4, 2, 6]
digit[9] = [9, 1]

for _ in range(T):
	a, b = map(int, sys.stdin.readline().split())
	a = int(str(a)[-1])
	if a in digit:
		idx = b % len(digit[a]) - 1
		print(digit[a][idx])
	elif a == 0:
		print(10)
	else:
		print(a)
