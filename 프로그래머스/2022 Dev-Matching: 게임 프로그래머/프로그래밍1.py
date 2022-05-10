day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
history = [0] * 366
ans = [0] * 5

def rank(money):
    if 0 <= money < 10000:
        return 0
    elif money < 20000:
        return 1
    elif money < 50000:
        return 2
    elif money < 100000:
        return 3
    else:
        return 4

def mdtd(m, d):
    ret = 0
    for i in range(m):
        ret += day[i]
    ret += d
    return ret

def solution(purchase):
    cur = 1
    for p in purchase:
        date, money = p.split()
        date = date.split('/')
        _, m, d = date
        m = int(m)
        d = int(d)
        real_day = mdtd(m, d)
        money = int(money)
        history[real_day] = money
    for i in range(1, 366):
        st = max(i - 30 + 1, 1)
        r = rank(sum(history[st:i + 1]))
        ans[r] += 1
    return ans