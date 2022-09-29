s = input()
for c in 'abcdefghijklmnopqrstuvwxyz':
    if c in s:
        print(s.index(c), end=' ')
    else:
        print(-1, end=' ')