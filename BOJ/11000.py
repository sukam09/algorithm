# TLE
def schedule(s, e):
    for i in range(len(end)):
        if s >= end[i]:
            end[i] = s
            return
    end.append(e)

N = int(input())
time = []
for _ in range(N):
    time.append(tuple(map(int, input().split())))
time.sort(key=lambda t: (t[1], t[0]))
end = []
for s, e in time:
    schedule(s, e)
print(len(end))