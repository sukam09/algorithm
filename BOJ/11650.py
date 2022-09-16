import sys

N = int(sys.stdin.readline())
xy = []
for _ in range(N):
    x, y = sys.stdin.readline().split()
    xy.append((int(x), int(y)))
xy = sorted(xy, key=lambda k: (k[0], k[1]))
xy = [str(x) + ' ' + str(y) for x, y in xy]
for i in xy: print(i)