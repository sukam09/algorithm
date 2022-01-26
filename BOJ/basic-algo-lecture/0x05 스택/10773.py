from sys import stdin
input = stdin.readline

k = int(input())
S = []
for _ in range(k):
    i = int(input())
    if i == 0:
        S.pop()
    else:
        S.append(i)
print(sum(S))