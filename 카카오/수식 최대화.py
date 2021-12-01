from itertools import permutations

def preprocess(exp):
    s = []
    op = set()
    cur = ''
    for e in exp:
        if e.isdigit():
            cur += e
        else:
            s.append(int(cur))
            s.append(e)
            op.add(e)
            cur = ''
    s.append(int(cur))
    return s, op

def process(s, op):
    res = []
    for i in s:
        res.append(i)
        if len(res) >= 3 and res[-2] == op:
            o2 = res.pop()
            res.pop()
            o1 = res.pop()
            res.append(calculate(o1, o2, op))
    return res

def calculate(o1, o2, op):
    if op == '+':
        return o1 + o2
    elif op == '-':
        return o1 - o2
    else:
        return o1 * o2

def solution(expression):
    ans = -1
    s, op = preprocess(expression)
    n = len(op)
    exp = s
    for p in permutations(op, n):
        s = exp
        for op in p:
            s = process(s, op)
        res = abs(int(s[0]))
        if res > ans:
            ans = res
    return ans