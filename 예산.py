def solution(d, budget):
    ans = 0
    cur = 0
    d.sort()
    for i in d:
        cur += i
        ans += 1
        if cur > budget:
            cur -= i
            ans -= 1
            break
    return ans