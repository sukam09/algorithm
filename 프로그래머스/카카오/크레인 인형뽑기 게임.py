def solution(board, moves):
    ans = 0
    s = []
    l = len(board)
    top = []
    for i in range(l):
        for j in range(l):
            if board[j][i]:
                top.append(j)
                break
    for m in moves:
        pos = m - 1
        if top[pos] == l:
            continue
        doll = board[top[pos]][pos]
        board[top[pos]][pos] = 0
        top[pos] += 1
        s.append(doll)
        if len(s) > 1 and s[-1] == s[-2]:
            ans += 2
            s.pop()
            s.pop()
    return ans