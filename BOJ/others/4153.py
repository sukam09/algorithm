import sys

while True:
    x, y, z = map(int, sys.stdin.readline().split())
    if x == y == z == 0:
        break
    
    side = [x, y, z]
    side_square = [d ** 2 for d in side if d != max(side)]
    if sum(side_square) == max(side) ** 2:
        print('right')
    else:
        print('wrong')
