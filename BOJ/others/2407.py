def C(n, m):
    cur = 1
    for i in range(1, m + 1):
        cur = cur * (n - i + 1) // i
    return cur

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
print(C(n, m))