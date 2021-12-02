from collections import defaultdict

def solution(rectangles):
    for i in range(len(rectangles)):
        rectangles[i] += [i + 1]
    rectangles.sort(key=lambda item: item[1])
    
    ylim = defaultdict(int)
    downed = []

    for x1, y1, x2, y2, idx in rectangles:
        h = y2 - y1
        ny = 0

        for i in range(x1, x2):
            ny = max(ylim[(i, i + 1)], ny)
        
        downed.append((x1, ny, x2, ny + h, idx))
        
        for i in range(x1, x2):
            ylim[(i, i + 1)] = ny + h
        
    downed.sort(key=lambda item: item[0])
    xlim = defaultdict(int)
    res = []

    for x1, y1, x2, y2, idx in downed:
        w = x2 - x1
        nx = 0

        for i in range(y1, y2):
            nx = max(xlim[(i, i + 1)], nx)
        
        res.append((nx, y1, nx + w, y2, idx))
        
        for i in range(y1, y2):
            xlim[(i, i + 1)] = nx + w
    
    res.sort(key=lambda item: item[4])
    ans = []
    for r in res:
        x1, y1, x2, y2 = r[:4]
        ans.append(str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2))
    return ans