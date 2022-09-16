from itertools import combinations

def solution(line):
    star = set()
    xs = set()
    ys = set()

    for p, q in combinations(line, 2):
        a, b, e = p
        c, d, f = q
        
        if a * d - b * c != 0:
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            
            if x == int(x) and y == int(y):
                x, y = int(x), int(y)
                star.add((x, y))
                xs.add(x)
                ys.add(y)
    
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    ans = []
    for i in range(ymax, ymin - 1, -1):
        row = ''
        for j in range(xmin, xmax + 1):
            row += '*' if (j, i) in star else '.'
        ans.append(row)
    
    return ans