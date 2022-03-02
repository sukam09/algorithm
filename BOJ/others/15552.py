import sys

T = int(sys.stdin.readline())
input_list = [list(sys.stdin.readline().split()) for _ in range(T)]
for i in range(T):
    print(int(input_list[i][0]) + int(input_list[i][1]))