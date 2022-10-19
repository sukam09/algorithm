tc = int(input())
for i in range(1, tc + 1):
    a, b = map(int, input().split())
    ans = -1 if a >= 10 or b >= 10 else a * b
    print("#%d %d" % (i, ans))