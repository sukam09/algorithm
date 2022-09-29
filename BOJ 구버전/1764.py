input = __import__('sys').stdin.readline
N, M = map(int, input().split())
NH = set([input().strip() for _ in range(N)])
NS = set([input().strip() for _ in range(M)])
ans = sorted(NH & NS)
print(len(ans))
for x in ans: print(x)