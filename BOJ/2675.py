T = int(input())
str_list = [list(input().split()) for _ in range(T)]
for str in str_list:
	R, S = int(str[0]), str[1]
	new_str = ''
	for s in S:
		new_s = s * R
		new_str += new_s
	print(new_str)