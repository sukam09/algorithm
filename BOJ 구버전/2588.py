i, j = int(input()), int(input())
old_j = j
d1 = j % 10
j //= 10
d2 = j % 10
j //= 10
d3 = j % 10
print(i * d1)
print(i * d2)
print(i * d3)
print(i * old_j)