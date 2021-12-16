from collections import defaultdict

def solution(rows, columns, connections, queries):
    graph = defaultdict(dict)

    for connection in connections:
        graph[(connection[0], connection[1])][(connection[2], connection[3])] = 1
        graph[(connection[2], connection[3])][(connection[0], connection[1])] = 1
    
    ans = []
    for x1, y1, x2, y2 in queries:
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        cnt = 0

        for i in range(ymin, ymax + 1):
            for x, y in graph[(xmin, i)].keys():
                if not graph[(xmin, i)][(x, y)]:
                    continue
                if not xmin <= x <= xmax or not ymin <= y <= ymax:
                    graph[(xmin, i)][(x, y)] = 0
                    graph[(x, y)][(xmin, i)] = 0
                    cnt += 1
            
            for x, y in graph[(xmax, i)].keys():
                if not graph[(xmax, i)][(x, y)]:
                    continue
                if not xmin <= x <= xmax or not ymin <= y <= ymax:
                    graph[(xmax, i)][(x, y)] = 0
                    graph[(x, y)][(xmax, i)] = 0
                    cnt += 1

        for i in range(xmin, xmax + 1):
            for x, y in graph[(i, ymin)].keys():
                if not graph[(i, ymin)][(x, y)]:
                    continue
                if not xmin <= x <= xmax or not ymin <= y <= ymax:
                    graph[(i, ymin)][(x, y)] = 0
                    graph[(x, y)][(i, ymin)] = 0
                    cnt += 1
            
            for x, y in graph[(i, ymax)].keys():
                if not graph[(i, ymax)][(x, y)]:
                    continue
                if not xmin <= x <= xmax or not ymin <= y <= ymax:
                    graph[(i, ymax)][(x, y)] = 0
                    graph[(x, y)][(i, ymax)] = 0
                    cnt += 1

        ans.append(cnt)
    
    return ans