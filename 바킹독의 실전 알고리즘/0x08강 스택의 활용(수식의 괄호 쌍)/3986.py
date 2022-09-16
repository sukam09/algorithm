from sys import stdin
input = stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    s = input().rstrip()
    S = []
    for c in s:
        if S and S[-1] == c:
            S.pop()
        else:
            S.append(c)
    ans += int(not S)
print(ans)