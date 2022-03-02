from collections import defaultdict

N = int(input())
vocab_list = [input() for _ in range(N)]
count = 0

for vocab in vocab_list:
	is_group = True
	last = ''
	checker = defaultdict(int)
	
	for char in vocab:
		if last != char and checker[char] >= 1:
			is_group = False
			break
		last = char
		checker[char] += 1
	
	if is_group:
		count += 1
		
print(count)