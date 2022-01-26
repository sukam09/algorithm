from sys import stdin
input = stdin.readline

def solve():
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for y in b:
        for x in a:
            if x > y:
                ans += 1
            else:
                break
    print(ans)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve()