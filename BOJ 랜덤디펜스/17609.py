import sys
input = sys.stdin.readline

def solve(s, deleted, st, en):
    while st < en:
        if s[st] == s[en]:
            st += 1
            en -= 1
        else:
            if not deleted and (solve(s, 1, st + 1, en) == 0 or solve(s, 1, st, en - 1) == 0):
                return 1
            else:
                return 2
    return 0

t = int(input())
for _ in range(t):
    s = input().rstrip()
    n = len(s)
    print(solve(s, 0, 0, n - 1))