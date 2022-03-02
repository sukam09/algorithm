from collections import deque

def solution():
    while q:
        route = q.popleft()
        cur = route[-1]
        now = times[cur]
        for next in cur - 1, cur + 1, cur * 2:
            if 0 <= next <= K + 1:
                if times[next] == float('inf'):
                    q.append(route + [next])
                    times[next] = now + 1
            if next == K:
                return times[next], route + [next]

N, K = map(int, input().split())
times = [float('inf')] * 100002
q = deque([[N]])
times[N] = 0
if N == K:
    print(0)
    print(N)
elif N > K:
    print(N - K)
    print(*[i for i in range(N, K - 1, -1)])
else:
    time, route = solution()
    print(time)
    print(*route)