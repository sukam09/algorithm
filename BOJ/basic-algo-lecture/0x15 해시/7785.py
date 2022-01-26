input = __import__('sys').stdin.readline

n = int(input())
s = set()
for _ in range(n):
    op = input().split()
    if op[1] == 'enter':
        s.add(op[0])
    else:
        s.remove(op[0])
for x in sorted(s, reverse=True):
    print(x)