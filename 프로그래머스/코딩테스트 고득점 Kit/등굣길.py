def solution(m, n, puddles):
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    grid[1][1] = 1
    new_puddles = set()
    
    if len(puddles[0]):
        for x, y in puddles:
            new_puddles.add((y, x))
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) != (1, 1) and (i, j) not in new_puddles:
                down = grid[i - 1][j]
                right = grid[i][j - 1]
                grid[i][j] = down + right

    return grid[n][m] % (10 ** 9 + 7)