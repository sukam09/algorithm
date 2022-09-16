def right(p):
    s = []
    for c in p:
        if c == '(':
            s.append(c)
        else:
            if s:
                s.pop()
            else:
                return False
    return s == []

def uv(p):
    if not p or right(p):
        return p
    op, cp = 0, 0
    for i, c in enumerate(p):
        if c == '(':
            op += 1
        if c == ')':
            cp += 1
        if op == cp > 0:
            tar = i
            break
    u = p[:tar + 1]
    v = p[tar + 1:]
    return u, v

def reverse(p):
    res = ''
    for c in p:
        if c == '(':
            res += ')'
        else:
            res += '('
    return res

def solution(p):
    if not p or right(p):
        return p
    u, v = uv(p)
    if right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])