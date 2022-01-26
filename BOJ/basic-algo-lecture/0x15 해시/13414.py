input = __import__('sys').stdin.readline
mis = lambda: map(int, input().split())
ii = lambda: int(input())

k, l = mis()
order = []
idx = {}
for i in range(l):
    n = input().rstrip()
    order.append(n)
    idx[n] = i
for i, x in enumerate(order):
    if i == idx[x]:
        print(x)
        k -= 1
    if k == 0:
        break