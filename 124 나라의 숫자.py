def ternary(n, cnt, country124):
    res = ''
    while n:
        res = country124[n % 3] + res
        n //= 3
    res = res.rjust(cnt, '1')
    return res

def solution(n):
    country124 = ['1', '2', '4']
    cnt = 1
    s = 0
    
    while True:
        s += 3 ** cnt
        if s >= n:
            break
        cnt += 1
    
    idx = n - (s - 3 ** cnt) - 1
    ans = ternary(idx, cnt, country124)
    return ans