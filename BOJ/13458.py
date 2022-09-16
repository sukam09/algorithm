from math import ceil

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = N
for a in A:
    a -= B
    if a > 0:
        ans += ceil(a / C)
print(ans)