A, B = map(int, input().split())
if A == B:
    result = '=='
else:
    result = '>' if A > B else '<'
print(result)