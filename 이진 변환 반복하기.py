def solution(s):
    cnt, zero = 0, 0
    while s != '1':
        res = ''
        for c in s:
            if c == '0':
                zero += 1
            else:
                res += c
        s = bin(len(res))[2:]
        cnt += 1
    return [cnt, zero]