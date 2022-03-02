def hansu(N):
	num = str(N)
	l = len(num)
	if l <= 2:
		return True
	else:
		diff = int(num[1]) - int(num[0])
		for i in range(2, l):
			d = int(num[i]) - int(num[i - 1])
			if d != diff:
				return False
		return True
 
N = int(input())
count = 0
 
for i in range(1, N + 1):
	if hansu(i):
		count += 1
 
print(count)