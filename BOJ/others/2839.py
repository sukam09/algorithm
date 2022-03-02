import sys

N = int(sys.stdin.readline())
five = N // 5
while five >= 0:
	if (N - five * 5) % 3 == 0:
		three = (N - five * 5) // 3
		print(five + three)
		break
	else:
		five -= 1

if five == -1:
	print(-1)
