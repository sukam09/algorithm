from collections import defaultdict

input = __import__('sys').stdin.readline
n = int(input())
net = defaultdict(list)
visited = [0]*(n+1)
for _ in range(int(input())):
    i, j = map(int, input().split())
    net[i].append(j); net[j].append(i)
s = [1]; visited[1] = 1
while s:
    cur = s.pop()
    for next in net[cur]:
        if not visited[next]: s.append(next); visited[next] = 1
print(sum(visited)-1)