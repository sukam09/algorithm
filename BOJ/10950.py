T = int(input())
input_list = [list(map(int, input().split())) for _ in range(T)]
for i in range(T):
    print(input_list[i][0] + input_list[i][1])