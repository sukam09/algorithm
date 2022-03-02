from collections import Counter

word = input().upper()
counter = [w for w in word]
counter = Counter(counter)
key_list = list(counter.keys())
count_list = list(counter.values())
maxval = max(count_list)
maxval_list = [x for x in key_list if counter[x] == maxval]
if len(maxval_list) == 1:
	print(maxval_list[0])
else:
	print('?')