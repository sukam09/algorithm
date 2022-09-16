N = int(input())
signal = input()
siglst = []
for i in range(5):
    siglst.append(signal[N // 5 * i:N // 5 * (i + 1)])
res = ''
for i in range(N // 5):
    for s in siglst:
        res += s[i]
    if res == '.' * 5:
        res = ''
        continue
    else:
        if res == '######...######':
            print(0, end='')
            res = ''
        elif res == '#####.....' or (res == '#####' and i == N // 5 - 1):
            print(1, end='')
            res = ''
        elif res == '#.####.#.####.#':
            print(2, end='')
            res = ''
        elif res == '#.#.##.#.######':
            print(3, end='')
            res = ''
        elif res == '###....#..#####':
            print(4, end='')
            res = ''
        elif res == '###.##.#.##.###':
            print(5, end='')
            res = ''
        elif res == '######.#.##.###':
            print(6, end='')
            res = ''
        elif res == '#....#....#####':
            print(7, end='')
            res = ''
        elif res == '######.#.######':
            print(8, end='')
            res = ''
        elif res == '###.##.#.######':
            print(9, end='')
            res = ''