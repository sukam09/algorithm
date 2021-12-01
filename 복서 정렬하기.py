def solution(weights, head2head):
    n = len(weights)
    wh = [0] * n
    wr = [0] * n
    for i in range(n):
        w = 0
        g = 0
        for j in range(n):
            if head2head[i][j] == 'N':
                continue
            g += 1
            if head2head[i][j] == 'W':
                w += 1
                if weights[j] > weights[i]:
                    wh[i] += 1
        wr[i] = w / g if g else 0
    ans = sorted([(wr, wh, w, i) for wr, wh, w, i in zip(wr, wh, weights, range(n))], key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    ans = [x[3] + 1 for x in ans]
    return ans