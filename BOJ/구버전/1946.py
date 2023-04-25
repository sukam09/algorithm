from sys import stdin

input = stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    score = sorted([tuple(map(int, input().split())) for _ in range(N)])
    ans = 1
    minval = score[0][1]
    for i in range(1, N):
        if score[i][1] < minval:
            minval = score[i][1]
            ans += 1
    print(ans)