def solution(s):
    ans = ''
    first = True
    for c in s:
        if first and c != ' ':
            ans += c.upper()
            first = False
        elif c == ' ':
            ans += c
            first = True
        else:
            ans += c.lower()
    return ans