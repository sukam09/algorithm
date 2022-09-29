def getk(n, k):
    cnt = 0; l = 1
    while n // k ** l:
        cnt += n // k ** l; l += 1
    return cnt

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
t1, t2, t3 = getk(n, 2), getk(n - m, 2), getk(m, 2)
f1, f2, f3 = getk(n, 5), getk(n - m, 5), getk(m, 5)
print(min(t1 - t2 - t3, f1 - f2 - f3))