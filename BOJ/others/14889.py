from itertools import combinations
input = __import__('sys').stdin.readline
N = int(input())
S1 = [[0] * (N + 1)]
S2 = [[0] + list(map(int, input().split())) for _ in range(N)]
S = S1 + S2
C = list(combinations(range(1, N + 1), N // 2))
team = C[:len(C) // 2]
diff = []
for x in team:
    enemy = tuple(set(range(1, N + 1)) - set(x))
    teamstat, enemystat = 0, 0
    for i in x:
        for j in x: teamstat += S[i][j]
    for i in enemy:
        for j in enemy: enemystat += S[i][j]
    diff.append(abs(teamstat - enemystat))
print(min(diff))