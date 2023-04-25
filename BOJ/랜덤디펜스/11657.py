import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
dist = [float('inf')] * (n + 1)
dist[1] = 0
for i in range(n):
    for a, b, c in edges:
        if dist[a] == float('inf'): continue
        if dist[a] + c < dist[b]:
            if i == n - 1:
                print(-1)
                sys.exit(0)
            dist[b] = dist[a] + c
for i in range(2, n + 1):
    print(dist[i] if dist[i] != float('inf') else -1)