def hanoi(n, s, v, g):
    if n == 1:
        return [[s, g]]
    else:
        return hanoi(n - 1, s, g, v) + [[s, g]] + hanoi(n - 1, v, s, g)

def solution(n):
    return hanoi(n, 1, 2, 3)