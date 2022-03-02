from collections import Counter

N, M = map(int, input().split())
DNA = [input() for _ in range(N)]
ans = []
dist = 0
for i in range(M):
    s = []
    for j in range(N):
        s.append(DNA[j][i])
    c = sorted(Counter(s).items(), key=lambda item: (-item[1], item[0]))[0]
    ans.append(c[0])
    dist += N - c[1]
print(''.join(ans))
print(dist)