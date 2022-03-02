s = input().split()
head = s[0]
tail = s[1:]
for t in tail:
    for i, c in enumerate(t):
        if not c.isalpha():
            target = i
            break
    ans = head + t[-2:target-1:-1].replace('][', '[]') + ' ' + t[:target] + ';'
    print(ans)