from collections import deque

def solution(numbers, target):
    ans = 0
    l = len(numbers)
    q = deque([(0, numbers[0]), (0, -numbers[0])])
    while q:
        idx, val = q.popleft()
        if idx < l - 1:
            q.append((idx + 1, val + numbers[idx + 1]))
            q.append((idx + 1, val - numbers[idx + 1]))
        elif val == target:
            ans += 1
    return ans