import sys

N = int(sys.stdin.readline())
coordinates = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))

ans = sorted(coordinates, key=lambda item: (item[1], item[0]))
for x, y in ans:
    print("%d %d" % (x, y))