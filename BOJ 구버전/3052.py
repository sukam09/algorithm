from collections import defaultdict

remainder = defaultdict(int)
for _ in range(10):
    n = int(input())
    r = n % 42
    remainder[r] += 1
print(len(remainder))