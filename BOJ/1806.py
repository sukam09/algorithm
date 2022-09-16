N, S = map(int, input().split())
seq = list(map(int, input().split()))
ans = float('inf')
start = 0; end = 0; target = seq[0]
while start < N:
    if target < S and end < N-1: end += 1; target += seq[end]
    else:
        if target >= S and end-start+1 < ans: ans = end-start+1
        target -= seq[start]; start += 1
print(ans if ans < float('inf') else 0)