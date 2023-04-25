num = input().split()
rev = [x[::-1] for x in num]
ans = rev[0] if int(rev[0]) > int(rev[1]) else rev[1]
print(ans)