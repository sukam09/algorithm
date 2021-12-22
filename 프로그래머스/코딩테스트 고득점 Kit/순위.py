from collections import defaultdict

def solution(n, results):
    wins = defaultdict(set)
    loses = defaultdict(set)

    for winner, loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)

    for i in range(1, n + 1):
        # 나한테 진 애들은 내가 진 애들한테도 졌음
        for loser in wins[i]:
            loses[loser] |= loses[i]
        
        # 나를 이긴 애들은 내가 이긴 애들도 이겼음
        for winner in loses[i]:
            wins[winner] |= wins[i]

    ans = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            ans += 1

    return ans