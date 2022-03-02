import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
	H, W, N = map(int, sys.stdin.readline().split())
	room = math.ceil(N / H)
	room = '0' + str(room) if room < 10 else str(room)
	height = N % H
	height = str(H) if height == 0 else str(height)
	print(height + room)