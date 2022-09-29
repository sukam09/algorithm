N = int(input())
W = sorted([int(input()) for _ in range(N)])
ans = 0
for i in range(len(W)):
    w = W[i] * (len(W) - i)
    if w > ans:
        ans = w
print(ans)