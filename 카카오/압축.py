def compress(msg, dic, ans):
    for i in range(1, len(msg) + 1):
        if msg[:i] not in dic:
            dic[msg[:i]] = len(dic) + 1
            w = msg[:i - 1]
            ans.append(dic[w])
            return w, ans
    ans.append(dic[msg])
    return msg, ans

def solution(msg):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = dict(zip(alpha, range(1, 27)))
    ans = []
    while msg:
        w, ans = compress(msg, dic, ans)
        msg = msg.replace(w, '', 1) 
    return ans