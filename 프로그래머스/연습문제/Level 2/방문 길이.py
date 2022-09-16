def move(x, y, dx, dy, trace):
    nx, ny = x + dx, y + dy
    
    if -5 <= nx <= 5 and -5 <= ny <= 5:
        trace[(x, y, nx, ny)] = 1
        trace[(nx, ny, x, y)] = 1
        return nx, ny
    else:
        return x, y

def solution(dirs):
    x, y = 0, 0
    trace = {}
    
    for dir in dirs:
        if dir == 'U':
            dx, dy = 0, 1
        elif dir == 'D':
            dx, dy = 0, -1
        elif dir == 'R':
            dx, dy = 1, 0
        else:
            dx, dy = -1, 0
        
        x, y = move(x, y, dx, dy, trace)

    return len(trace) // 2