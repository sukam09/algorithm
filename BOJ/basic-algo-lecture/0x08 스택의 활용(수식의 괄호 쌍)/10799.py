input = __import__('sys').stdin.readline

s = input().rstrip()
cnt = 0
ans = 0
for i, c in enumerate(s):
    if c == '(':
        cnt += 1
    else:
        cnt -= 1
        if s[i - 1] == '(':
            ans += cnt
        else:
            ans += 1
print(ans)