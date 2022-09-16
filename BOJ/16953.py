from collections import deque

A, B = map(int, input().split())
q = deque([A])
operations = {A: 1}
ans = -1
while q:
    target = q.popleft()
    cur = operations[target]
    if target * 2 == B or target * 10 + 1 == B:
        ans = cur + 1
        break
    if 2 * target <= B:
        q.append(2 * target)
        operations[2 * target] = cur + 1
    if target * 10 + 1 <= B:
        q.append(target * 10 + 1)
        operations[target * 10 + 1] = cur + 1
print(ans)