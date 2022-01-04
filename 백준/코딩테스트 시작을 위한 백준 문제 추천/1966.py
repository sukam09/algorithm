from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque()
    priorities = list(map(int, input().split()))
    for i, val in enumerate(priorities):
        q.append((val, i))
    
    rank = 1
    while len(q) > 1:
        p = [x[0] for x in q]
        if max(p[1:]) > q[0][0]:
            q.rotate(-1)
        else:
            i = q.popleft()[1]
            if i == m:
                print(rank)
                break
            rank += 1
    else:
        print(rank)