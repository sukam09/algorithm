from collections import deque

def solution():
    while q:
        cur = q.popleft()
        now = times[cur]
        for next in cur - 1, cur + 1, cur * 2:
            if next == K:
                return now + 1
            if 0 <= next <= K + 1:
                if times[next] == float('inf'):
                    q.append(next)
                    times[next] = now + 1

N, K = map(int, input().split())
times = [float('inf')] * 100002
q = deque([N])
times[N] = 0
if N == K:
    print(0)
elif N > K:
    print(N - K)
else:
    print(solution())