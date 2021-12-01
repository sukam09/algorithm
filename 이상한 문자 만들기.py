def solution(s):
    ans = ''
    i = 0
    for c in s:
        if c == ' ':
            i = 0
            ans += c
            continue
        ans += c.upper() if i % 2 == 0 else c.lower()
        i += 1
    return ans