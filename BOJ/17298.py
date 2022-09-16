input = __import__('sys').stdin.readline
N = int(input())
A = list(map(int, input().split()))
if N > 1:
    S = []
    ans = [0] * N
    S.append((0, A[0]))
    for i in range(1, len(A)):
        cur = A[i]
        if cur > S[-1][1]:
            while S and cur > S[-1][1]:
                ans[S.pop()[0]] = cur
        S.append((i, cur))
    A[-1] = cur
    while S:
        i, val = S.pop()
        ans[i] = cur if cur > val else -1
    print(*ans)
else: print(-1)