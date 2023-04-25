input = __import__('sys').stdin.readline
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
idx = N-1; cnt = 0
while K:
    if A[idx] <= K:
        q = K // A[idx]
        K -= A[idx]*q; cnt += q; idx -= 1
    elif idx: idx -= 1
    else: break
print(cnt)