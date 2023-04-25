import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
pos = []
neg = []
mx = 0
for b in books:
    if b > 0:
        pos.append(b)
    else:
        neg.append(abs(b))
    mx = max(mx, abs(b))
pos.sort(reverse=1)
neg.sort(reverse=1)
ans = 0
for i in range(0, len(pos), m):
    ans += pos[i] * 2
for i in range(0, len(neg), m):
    ans += neg[i] * 2
ans -= mx
print(ans)