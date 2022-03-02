def get_time(alpha):
	idx = ord(alpha) - ord('A')
	
	if idx <= 2:
		time = 3
	elif idx <= 5:
		time = 4
	elif idx <= 8:
		time = 5
	elif idx <= 11:
		time = 6
	elif idx <= 14:
		time = 7
	elif idx <= 18:
		time = 8
	elif idx <= 21:
		time = 9
	else:
		time = 10
	
	return time

str = input()
total_time = 0
for s in str:
	time = get_time(s)
	total_time += time
print(total_time)