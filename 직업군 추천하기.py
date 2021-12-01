def solution(table, languages, preference):
    field = {}
    for t in table:
        t = t.split()
        field[t[0]] = dict(zip(t[1:], range(5, 0, -1)))
    lp = dict(zip(languages, preference))
    fs = {}
    for f in field:
        total = 0
        for l in lp:
            try:
                total += lp[l] * field[f][l]
            except:
                pass
        fs[f] = total
    ans = sorted([f for f, s in fs.items() if s == max(fs.values())])[0]
    return ans