n, k = map(int, input().split())
divisor = [x for x in range(1, n + 1) if n % x == 0]
ans = 0 if len(divisor) < k else divisor[k - 1]
print(ans)