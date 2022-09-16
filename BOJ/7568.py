import sys

N = int(sys.stdin.readline())
weight, height = [], []

for _ in range(N):
    w, h = map(int, sys.stdin.readline().split())
    weight.append(w)
    height.append(h)

for record in zip(weight, height):
    my_weight, my_height = record[0], record[1]
    deongchi = [
        1 if x > my_weight and y > my_height else 0
        for x, y in zip(weight, height) 
    ]
    print(sum(deongchi) + 1, end = ' ')