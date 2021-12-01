from collections import deque


def solution(record):
    q = deque()
    s = []

    fifo_val = 0
    lifo_val = 0

    for rec in record:
        act, val, num = rec.split()
        val = int(val)
        num = int(num)

        if act == 'P':
            for _ in range(num):
                q.append(val)
                s.append(val)
        else:
            for _ in range(num):
                fifo_val += q.popleft()
                lifo_val += s.pop()
    
    return [fifo_val, lifo_val]