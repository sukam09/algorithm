from collections import defaultdict

def solution(n, computers):
    ans = 0
    visited = [0]*n
    net = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i!=j:
                net[i].append(j)
    while sum(visited) < n:
        for i in range(n):
            if not visited[i]:
                cur = i
                s = [cur]
                visited[cur] = 1
                break
        while s:
            cur = s.pop()
            for next in net[cur]:
                if not visited[next]:
                    s.append(next)
                    visited[next] = 1
        ans += 1
    return ans