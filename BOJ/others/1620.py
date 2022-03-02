input = __import__('sys').stdin.readline
N, M = map(int, input().split())
L = [input().strip() for _ in range(N)]
dic = dict(zip(range(1, N + 1), L))
rdic = {v: k for k, v in dic.items()}
for _ in range(M):
    q = input().strip()
    if q.isalpha(): print(rdic[q])
    else: print(dic[int(q)])