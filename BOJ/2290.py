def LCD(step, i):
    if step == 1:
        return ' ' + ' ' * s + ' ' if i == 1 or i == 4 else ' ' + '-' * s + ' '
    elif step == 2:
        if i == 4 or i == 8 or i == 9 or i == 0:
            return '|' + ' ' * s + '|'
        elif i == 1 or i == 2 or i == 3 or i == 7:
            return ' ' + ' ' * s + '|'
        else:
            return '|' + ' ' * s + ' '
    elif step == 3:
        return ' ' + ' ' * s + ' ' if i == 1 or i == 7 or i == 0 else ' ' + '-' * s + ' '
    elif step == 4:
        if i == 6 or i == 8 or i == 0:
            return '|' + ' ' * s + '|'
        elif i == 2:
            return '|' + ' ' * s + ' '
        else:
            return ' ' + ' ' * s + '|'
    else:
        return ' ' + ' ' * s + ' ' if i == 1 or i == 4 or i == 7 else ' ' + '-' * s + ' '

s, n = map(int, input().split())
n = list(map(int, str(n)))
for i in range(1, 6):
    if i == 2 or i == 4:
        for _ in range(s):
            for j in n:
                print(LCD(i, j), end=' ')
            print()
    else:
        for j in n:
            print(LCD(i, j), end=' ')
        print()