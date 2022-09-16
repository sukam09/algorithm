import sys

while True:
	n = int(sys.stdin.readline())
	if n == 0:
		break
	elif n == int(str(n)[::-1]):
		print('yes')
	else:
		print('no')
