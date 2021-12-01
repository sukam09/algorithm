def solution(files):
    ans = []

    for f in files:
        start, end = -1, -1
        cnt = 0
        for i, c in enumerate(f):
            if cnt == 5 or (cnt and not c.isdigit()):
                end = i
                break
            if c.isdigit():
                cnt += 1
                if start == -1:
                    start = i
        if end == -1:
            end = len(f)
        
        head, number, tail = f[:start], f[start:end], f[end:]
        ans.append((head, number, tail))

    ans.sort(key=lambda item: (item[0].lower(), int(item[1])))
    ans = list(map(lambda item: item[0] + item[1] + item[2], ans))
    return ans