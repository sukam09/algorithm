import sys

T = int(sys.stdin.readline())
BVPS = '()'
for _ in range(T):
    PS = sys.stdin.readline().rstrip()
    while BVPS in PS:
        PS = PS.replace(BVPS, '')
    if PS == '':
        print("YES")
    else:
        print("NO")