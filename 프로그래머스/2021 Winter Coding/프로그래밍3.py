def solution(cakes, cut_rows, cut_columns):
    n = len(cakes)
    rows = []
    columns = []

    start = 0
    for cr in cut_rows:
        rows.append((start, cr))
        start = cr
    rows.append((start, n))
    
    start = 0
    for cc in cut_columns:
        columns.append((start, cc))
        start = cc
    columns.append((start, n))

    ans = 1
    for row in rows:
        rs, re = row
        for col in columns:
            cs, ce = col
            res = set()
            for r in range(rs, re):
                for c in range(cs, ce):
                    res.add(cakes[r][c])
            ans = max(ans, len(res))

    return ans