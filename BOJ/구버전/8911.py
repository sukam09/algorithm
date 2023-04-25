def move(x, y, d, i):
    if d == 0:
        y += i * 1
    elif d == 1:
        x += i * 1
    elif d == 2:
        y -= i * 1
    else:
        x -= i * 1
    return x, y

for _ in range(int(input())):
    ctrlprog = input()
    x = y = 0
    d = 0
    px, py, nx, ny = 0, 0, 0, 0
    for c in ctrlprog:
        if c == 'F':
            x, y = move(x, y, d, 1)
        elif c == 'B':
            x, y = move(x, y, d, -1)
        elif c == 'L':
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
        if x > 0 and abs(x) > px:
            px = abs(x)
        if y > 0 and abs(y) > py:
            py = abs(y)
        if x < 0 and abs(x) > nx:
            nx = abs(x)
        if y < 0 and abs(y) > ny:
            ny = abs(y)
    print((px + nx) * (py + ny))