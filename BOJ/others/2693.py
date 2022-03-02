num_list = [list(map(int, input().split())) for _ in range(int(input()))]
for num in num_list:
    print(sorted(num)[-3])