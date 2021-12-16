def solution(money):
    ans = 0
    n = len(money)
    ans1, ans2 = [], []
    for i, x in enumerate(money):
        ans2.append(x) if i % 2 else ans1.append(x)
    if n % 2 == 0:
        ans = max(sum(ans1), sum(ans2))
    else:
        # Cannot solve this problem using greedy
        pass
    return ans

# money = [
#     [1, 2, 3, 1],  # 4
#     [1, 3, 2],  # 3
#     [1, 2, 3, 4, 5],  # 8
#     [2, 4, 6, 1, 2, 0],  # 10
#     [1, 2, 3, 1, 2, 3, 1, 2],  # 8
#     [1, 2, 10, 10, 10, 20, 1, 2],  # 34
#     [200, 200, 20, 3, 300, 350, 70, 35]  # 590
# ]