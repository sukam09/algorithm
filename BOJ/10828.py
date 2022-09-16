from sys import stdin
input = stdin.readline

n = int(input())
s = []

for _ in range(n):
    cmd = input().split()
    
    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
        s.append(cmd[1])
    elif cmd[0] == 'pop':
        print(s.pop()) if s else print(-1)
    elif cmd[0] == 'size':
        print(len(s))
    elif cmd[0] == 'empty':
        print(int(not s))
    else:
        print(s[-1]) if s else print(-1)