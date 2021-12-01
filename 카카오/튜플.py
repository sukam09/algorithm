def solution(s):
    s = s[1:-1]
    stack = []
    res = ''
    for c in s:
        if c == '{':
            element = True
        elif c == '}':
            stack.append(res.split(','))
            res = ''
            element = False
        elif element:
            res += c
    stack.sort(key=lambda item: len(item))
    vis = [0] * 100001
    ans = []
    for st in stack:
        for i in st:
            i = int(i)
            if not vis[i]:
                ans.append(i)
                vis[i] = 1
    return ans