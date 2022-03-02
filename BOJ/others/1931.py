input = __import__('sys').stdin.readline
N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))
time.sort(key=lambda x: (x[1], x[0]))
cur = 0; cnt = 0
for s, e in time:
    if s >= cur: cur = e; cnt += 1
print(cnt)