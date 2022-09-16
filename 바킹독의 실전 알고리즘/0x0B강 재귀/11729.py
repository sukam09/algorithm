from sys import stdin
input = stdin.readline

def hanoi(n, s, v, g):
    if n == 1:
        return [[s, g]]
    else:
        return hanoi(n - 1, s, g, v) + [[s, g]] + hanoi(n - 1, v, s, g)

n = int(input())
print(2 ** n - 1)
for s, g in hanoi(n, 1, 2, 3):
    print(s, g)