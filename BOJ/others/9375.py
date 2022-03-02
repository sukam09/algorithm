input = __import__('sys').stdin.readline
n = int(input())
for _ in range(n):
    T = int(input())
    dic = {}
    for _ in range(T):
        c, ct = input().split()
        if ct in dic: dic[ct].append(c)
        else: dic[ct] = ['no', c]
    ans = 1
    for k in dic: ans *= len(dic[k])
    print(ans - 1)