from collections import deque

def right(s, op, pair):
    stack = []

    for c in s:
        if c in op:
            stack.append(c)
        elif stack and stack[-1] == pair[c]:
            stack.pop()
        else:
            return False
    
    return stack == []

def solution(s):
    s = deque(s)
    op = ['(', '[', '{']
    pair = {')': '(', ']': '[', '}': '{'}

    ans = 0
    ans += right(s, op, pair)

    for _ in range(len(s) - 1):
        s.rotate(-1)
        ans += right(s, op, pair)
    
    return ans