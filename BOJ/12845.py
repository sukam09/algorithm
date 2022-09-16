n = int(input())
L = list(map(int, input().split()))
print(max(L) * (n - 2) + sum(L))