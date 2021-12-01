def solution(s, n):
    ans = ''
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    little = 'abcdefghijklmnopqrstuvwxyz'
    for c in s:
        if c != ' ':
            if c.isupper():
                ans += big[(ord(c) - ord('A') + n) % 26]
            else:
                ans += little[(ord(c) - ord('a') + n) % 26]
        else:
            ans += c
    return ans