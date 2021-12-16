def invalid(ans):
    for x, y, a in ans:
        if a == 0:
            if y > 0 and (x - 1, y, 1) not in ans and (x, y, 1) not in ans and (x, y - 1, 0) not in ans:
                return True
        else:
            if (x, y - 1, 0) not in ans and (x + 1, y - 1, 0) not in ans and ((x - 1, y, 1) not in ans \
                                        or (x + 1, y, 1) not in ans):
                return True
    return False

def solution(n, build_frame):
    ans = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1:
            ans.add(item)
            if invalid(ans):
                ans.remove(item)
        else:
            ans.remove(item)
            if invalid(ans):
                ans.add(item)
    
    return sorted(list(map(list, ans)))