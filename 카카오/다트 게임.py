def solution(dartResult):
    s = []
    cur = ''
    for dr in dartResult:
        if not dr.isdigit():
            if cur:
                s.append(int(cur))
                cur = ''
            if dr == 'D':
                s[-1] **= 2
            elif dr == 'T':
                s[-1] **= 3
            elif dr == '*':
                s[-1] *= 2
                if len(s) > 1:
                    s[-2] *= 2
            elif dr == '#':
                s[-1] = -s[-1]
        else:
            cur += dr
    return sum(s)