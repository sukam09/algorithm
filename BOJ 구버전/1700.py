from collections import deque, Counter

N, K = map(int, input().split())
order = deque(map(int, input().split()))
if K <= N:
    print(0)
else:
    ans = 0
    power = [0] * (K + 1)
    counter = Counter(order)
    for i in range(N):
        cur = order.popleft()
        power[cur] = 1
        counter[cur] -= 1
    while len(order) > 1:
        cur = order.popleft()
        counter[cur] -= 1
        if power[cur] == 0:
            candidate = sorted([c for c in counter.items() if power[c[0]] == 1], key=lambda item: item[1])
            target = candidate[0][0]
            power[target] = 0
            power[cur] = 1
            ans += 1
    if power[order.popleft()] == 0:
        ans += 1
    print(ans)