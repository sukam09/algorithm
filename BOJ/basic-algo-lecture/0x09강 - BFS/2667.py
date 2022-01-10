"""
1. 처음에 입력값을 받을 때 그대로 list에 넣으면 int가 아닌 str이 됨에 주의.
2. 마지막에 각 단지에 속하는 집의 수를 출력할 때 오름차순으로 출력해야 함에 주의.
3. 아니면 처음부터 입력받을 때 int로 바꿔서 받는 방법도 있다. 이 방법이 가장 나아 보인다.
"""

from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
grid = [list(map(int, input())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
village = 0
houses = []

for i in range(n):
    for j in range(n):
        if vis[i][j] or not grid[i][j]:
            continue

        village += 1 
        house = 0
        q = deque([(i, j)])
        vis[i][j] = 1

        while q:
            x, y = q.popleft()
            house += 1

            for nx, ny in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
                if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny]:
                    q.append((nx, ny))
                    vis[nx][ny] = 1
        
        houses.append(house)

print(village)
for house in sorted(houses):
    print(house)