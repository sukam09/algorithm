input = __import__('sys').stdin.readline
while True:
    i, j = map(int, input().split())
    if i == j == 0: break
    if i % j == 0: print("multiple")
    elif j % i == 0: print("factor")
    else: print("neither")