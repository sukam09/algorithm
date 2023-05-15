import sys

input = sys.stdin.readline


def solve(s, p):
    idx1 = 0
    idx2 = 0
    n = len(s)
    m = len(p)
    ans = 0
    while 1:
        if s[idx1] == p[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            ans += 1
            idx2 += 1
        if idx1 == n:
            return ans + m - idx2
        if idx2 == m:
            return "IMPOSSIBLE"


t = int(input())
for i in range(1, t + 1):
    s = input().rstrip()
    p = input().rstrip()
    print(f"Case #{i}: {solve(s, p)}")
