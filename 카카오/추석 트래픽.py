def get_ms(S):
    S = S.split(':')
    h, m, s = int(S[0]), int(S[1]), eval(S[2])
    ms = (h * 60 * 60 + m * 60 + s) * 1000
    return int(ms)

def solution(lines):
    timeline = []
    candidate = []
    
    for l in lines:
        l = l.split()
        S, T = l[1], eval(l[2][:-1])
        right = get_ms(S)
        left = int(right - T * 1000 + 1)
        timeline.append((left, right))
        candidate.append(left)
        candidate.append(right)

    ans = 0
    for c in candidate:
        wl, wr = c, c + 999
        cnt = 0
        for l, r in timeline:
            if not (r < wl or l > wr):
                cnt += 1
        ans = max(cnt, ans)
    
    return ans