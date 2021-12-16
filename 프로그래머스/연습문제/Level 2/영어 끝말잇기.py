from collections import deque

def solution(n, words):
    q = deque(words)
    turn = 1
    last = ''
    history = {}

    while q:
        for i in range(1, n + 1):
            cur = q.popleft()
            if last and (last[-1] != cur[0] or cur in history):
                return [i, turn]
            last = cur
            history[last] = 1
        turn += 1
    
    return [0, 0]