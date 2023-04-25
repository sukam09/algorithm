A, B, C = map(int, input().split())
ans = int(A / (C - B)) + 1 if C > B else -1
print(ans)
