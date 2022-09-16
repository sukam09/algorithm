import sys

def init(k, n):
	apt = [[0] * n] * (k + 1)
	apt[0] = [x + 1 for x in range(n)]
	for i in range(k + 1):
		apt[i][0] = 1
	return apt

def cal_person(apt, k, n):
	for i in range(1, k + 1):
		for j in range(1, n):
			apt[i][j] = apt[i - 1][j] + apt[i][j - 1]
	return apt[k][n - 1]

T = int(sys.stdin.readline())
for _ in range(T):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	apt = init(k, n)
	person = cal_person(apt, k, n)
	print(person)
