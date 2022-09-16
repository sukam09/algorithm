import sys
input = sys.stdin.readline

s = input().rstrip()
p = set()
for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        p.add(s[j:j + i])
print(len(p))