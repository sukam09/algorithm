from collections import defaultdict, deque

def bfs(tower, n, banned):
    vis = [0] * (n + 1)
    res = []

    for i in range(1, n + 1):
        if vis[i]:
            continue

        q = deque([i])
        vis[i] = 1
        cnt = 1

        while q:
            cur = q.popleft()
            for next in tower[cur]:
                start, end = min(cur, next), max(cur, next)
                if (start, end) != banned and not vis[next]:
                    q.append(next)
                    vis[next] = 1
                    cnt += 1
        
        res.append(cnt)

    return abs(res[0] - res[1])

def solution(n, wires):
    tower = defaultdict(list)
    ans = n
    edge = []
    
    for start, end in wires:
        tower[start].append(end)
        tower[end].append(start)
        if start < end:
            edge.append((start, end))
    
    for start, end in edge:
        banned = (start, end)
        ans = min(ans, bfs(tower, n, banned))

    return ans