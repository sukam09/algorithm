a, b, c, x, y = map(int, input().split())
ans = float('inf')

# half는 반반 치킨의 개수
# half가 2 * max(x, y)보다 커지면 치킨이 낭비되므로 딱 여기까지만 탐색
# 여기서 주의할 점은 x, y가 치킨의 최소 개수이므로 half // 2가 x 혹은 y 둘 중에 하나보다 큰 건 상관없음
for half in range(0, 2 * max(x, y) + 1, 2):
    # 치킨의 개수는 음수가 될 수 없음
    seasoned = max(x - half // 2, 0)
    fried = max(y - half // 2, 0)
    
    cost = a * seasoned + b * fried + c * half
    ans = min(cost, ans)

print(ans)