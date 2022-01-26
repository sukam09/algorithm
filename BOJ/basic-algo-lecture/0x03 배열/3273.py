from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
b = set()
ans = 0

for i, val in enumerate(a):
    if x > val and x - val in b:
        ans += 1
    b.add(val)

print(ans)