def solution(record):
    res = []
    id = {}
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            id[r[1]] = r[2]
            res.append((r[1], "님이 들어왔습니다."))
        elif r[0] == 'Leave':
            res.append((r[1], "님이 나갔습니다."))
        else:
            id[r[1]] = r[2]
    ans = []
    for r in res:
        ans.append(id[r[0]] + r[1])
    return ans