input = __import__('sys').stdin.readline
N = int(input())
X = list(map(int, input().split()))
new_X = sorted(set(X))
Y = {k: v for k, v in zip(new_X, range(N))}
for x in X:
    print(Y[x], end=' ')