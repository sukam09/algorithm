def solution(n, k, cmd):
    table = {}
    table[0] = [-1, 1]
    for i in range(1, n - 1):
        table[i] = [i - 1, i + 1]
    table[n - 1] = [n - 2, -1]
    recent = []

    for c in cmd:
        if c == 'C':
            front, back = table[k][0], table[k][1]
            recent.append((k, front, back))

            if back == -1:
                table[front][1] = -1
                del table[k]
                k = front
            else:
                if front != -1:
                    table[front][1] = back
                table[back][0] = front
                del table[k]
                k = back
        
        elif c == 'Z':
            target, front, back = recent.pop()
            table[target] = [front, back]
            if front != -1:
                table[front][1] = target
            if back != -1:
                table[back][0] = target
        
        else:
            step = int(c[2:])
            dir = 0 if c[0] == 'U' else 1
            for _ in range(step):
                k = table[k][dir]

    ans = ''
    for i in range(n):
        ans += 'O' if i in table else 'X'
    return ans