def solution(s):
    l = len(s)
    ans = l
    for i in range(1, l // 2 + 1):
        hist = ''
        res = ''
        cnt = 1
        for j in range(0, l, i):
            seg = s[j:j + i]
            if seg == hist:
                cnt += 1
            else:
                if cnt >= 2:
                    res += str(cnt)
                res += seg
                cnt = 1
            hist = seg
        if cnt >= 2:
            res += str(cnt)
        cl = len(res)
        if cl < ans:
            ans = cl
    return ans