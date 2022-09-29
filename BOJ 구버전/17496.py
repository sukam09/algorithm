N, T, C, P = map(int, input().split())
starfruits = 0
for i in range(1 + T, N + 1, T):
    starfruits += C
print(starfruits * P)