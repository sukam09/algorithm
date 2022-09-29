input_list = [list(map(int, input().split())) for i in range(10)]
max, num = 0, 0
for _, item in enumerate(input_list):
    num = num - item[0] + item[1]
    max = num if num > max else max
print(max)
