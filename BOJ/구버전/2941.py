c_alpha = ['c=', 'c-', 'dz', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
c_alpha_count = 0

for i in range(len(str) - 1):
	cur = str[i:i + 2]
	if cur in c_alpha:
		if cur == 'dz':
			try:
				count = 1 if str[i + 2] == '=' else 0
				c_alpha_count += count
			except IndexError:
				break
		else:
			c_alpha_count += 1

print(len(str) - c_alpha_count)
