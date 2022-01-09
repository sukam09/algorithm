from itertools import permutations

a, b = map(int, input().split())
ans = -1
a = str(a)

for p in permutations(a, len(a)):
    if p[0] == '0':
        continue
    num = int(''.join(p))
    if num < b:
        ans = max(num, ans)

print(ans)