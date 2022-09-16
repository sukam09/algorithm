from collections import deque

def conv(num, n):
    res = ''
    while num:
        res += chr(55 + num % n) if num % n >= 10 else str(num % n)
        num //= n
    return reversed(res)

def solution(n, t, m, p):
    cnt = m * (t - 1) + p
    seq = []
    num = 0
    q = deque(['0'])
    
    for _ in range(cnt):
        seq.append(q.popleft())
        if not q:
            num += 1
            convres = conv(num, n)
            for cr in convres:
                q.append(cr)
    
    ans = ''
    for i in range(p - 1, len(seq), m):
        ans += seq[i]
    return ans