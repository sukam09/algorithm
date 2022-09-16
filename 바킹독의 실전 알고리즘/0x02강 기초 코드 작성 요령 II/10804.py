from sys import stdin
input = stdin.readline

arr = list(range(21))
for _ in range(10):
    a, b = map(int, input().split())
    arr[a:b + 1] = arr[b:a - 1:-1]

for i in range(1, 21):
    print(arr[i], end=' ')