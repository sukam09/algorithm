from math import sqrt

d, h, w = map(int, input().split())
y = sqrt(d ** 2 / (1 + (w / h) ** 2))
x = w / h * y
print(int(y), int(x))