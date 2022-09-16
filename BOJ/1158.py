from collections import deque

input = __import__('sys').stdin.readline
N, K = map(int, input().split())
q = deque([x for x in range(1, N+1)])
ans = []
while q:
    for _ in range(K-1): q.rotate(-1)
    ans.append(q.popleft())
print("<" + ', '.join(map(str, ans)) + ">")