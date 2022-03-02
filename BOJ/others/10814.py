import sys

N = int(sys.stdin.readline())
members = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    members.append((age, name))
members = sorted(members, key=lambda x: x[0])
members = [str(x) + ' ' + y for x, y in members]
print('\n'.join(members))