import sys

N = int(sys.stdin.readline())
step, end = 1, 1

while end < N:
	end += 6 * step
	step += 1

print(step)
