import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d1 = {}
d2 = {}
for _ in range(n):
    team = input().rstrip()
    num = int(input())
    members = []
    for _ in range(num):
        member = input().rstrip()
        members.append(member)
        d2[member] = team
    d1[team] = sorted(members)
for _ in range(m):
    q1 = input().rstrip()
    q2 = int(input())
    if q2 == 0:
        for x in d1[q1]:
            print(x)
    else:
        print(d2[q1])