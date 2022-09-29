"""
1. q는 slicing할 수 없음에 주의
2. q[0]가 아니고 q[0][0]과 비교해야 함에 주의
3. 비교할 때 q에 있는 순서쌍 단위로 비교하면 i 때문에 틀림(즉, heap 하나만으로는 풀 수 없음)
"""

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