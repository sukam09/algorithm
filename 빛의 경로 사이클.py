def move(x, y, dx, dy, r, c, grid, right_vec, left_vec):
    x, y = (x + dx + r) % r, (y + dy + c) % c

    if grid[x][y] == 'L':
        dx, dy = left_vec[(dx, dy)]
    elif grid[x][y] == 'R':
        dx, dy = right_vec[(dx, dy)]

    return x, y, dx, dy

def solution(grid):
    r, c = len(grid), len(grid[0])
    right_vec = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    left_vec = dict(zip(right_vec.values(), right_vec.keys()))

    history = set()
    ans = []

    for i in range(r):
        for j in range(c):
            for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                cycle = set()
                x, y = i, j
                
                while (x, y, dx, dy) not in cycle:
                    if (x, y, dx, dy) in history:
                        break
                    
                    cycle.add((x, y, dx, dy))
                    history.add((x, y, dx, dy))
                    x, y, dx, dy = move(x, y, dx, dy, r, c, grid, right_vec, left_vec)
                
                else:
                    ans.append(len(cycle))

    return sorted(ans)