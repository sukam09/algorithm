N = int(input())
k = 2 * N - 1
for i in range(N, 0, -1):
    str = ('*' * (2 * i - 1)).center(k)
    print(str[:N + i])