from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
b = [0] * 200005
ans = 0

for i, val in enumerate(a):
    if x > val and b[x - val]:
        ans += 1
    b[val] += 1

print(ans)