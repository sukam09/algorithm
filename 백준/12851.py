from collections import deque

n, k = map(int, input().split())
vis = [0] * 100001
vis[n] = 1
q = deque([(n, 0)])
time = 0
route = 0

while q:
    v, t = q.popleft()
    # 굳이 중복체크를 큐에 들어갈 때가 아닌 큐에서 뺄 때 해야하는 이유..?
    vis[v] = 1

    # 최단시간이 산출되어 있고 현재 시간이 최단시간보다 크면 그 이후의 값부터는 볼 필요가 없음
    if time and t > time:
        break

    if v == k:
        time = t
        route += 1
        vis[v] = 0
    else:
        for nv in v - 1, v + 1, v * 2:
            if 0 <= nv <= 100000 and not vis[nv]:
                q.append((nv, t + 1))

print(time)
print(route)