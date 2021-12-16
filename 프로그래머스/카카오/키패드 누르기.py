def solution(numbers, hand):
    ans = ''
    l, r = (3, 0), (3, 2)
    for n in numbers:
        x, y = ((n - 1) // 3, (n - 1) % 3) if n else (3, 1)
        if y == 0:
            ans += 'L'
            l = x, y
        elif y == 2:
            ans += 'R'
            r = x, y
        else:
            ldist = abs(x - l[0]) + abs(y - l[1])
            rdist = abs(x - r[0]) + abs(y - r[1])
            if ldist < rdist:
                ans += 'L'
                l = x, y
            elif ldist > rdist:
                ans += 'R'
                r = x, y
            else:
                if hand == 'left':
                    ans += 'L'
                    l = x, y
                else:
                    ans += 'R'
                    r = x, y
    return ans