from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    s = input()
    val = 0
    
    for c in s:
        if c == '(':
            val += 1
        elif c == ')':
            val -= 1
        if val < 0:
            print("NO")
            break
    else:
        print("YES") if val == 0 else print("NO")