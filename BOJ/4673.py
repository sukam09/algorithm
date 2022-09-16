from collections import defaultdict

def d(n):
	num = [int(x) for x in str(n)]
	result = n + sum(num)
	return result

checker = defaultdict(bool)
for i in range(1, 10001):
    checker[d(i)] = True
self_number = [x for x in range(1, 10001) if not checker[x]]
for x in self_number: print(x)