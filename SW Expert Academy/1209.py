for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for i in range(100):
        ans = max(ans, sum(arr[i]))
    for j in range(100):
        s = sum(arr[j][k] for k in range(100))
        ans = max(ans, s)
    s = 0
    for i in range(100):
        s += arr[i][j]
    ans = max(ans, s)
    s = 0
    for i in range(100):
        s += arr[i][99 - i]
    ans = max(ans, s)
    print(f"#{t} {ans}")