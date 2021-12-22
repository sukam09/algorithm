def solution(n, results):
    graph = [[0] * n for _ in range(n)]

    for winner, loser in results:
        winner -= 1
        loser -= 1
        graph[winner][loser] = 1
        graph[loser][winner] = -1
    
    for me in range(n):
        wins = [enemy for enemy, res in enumerate(graph[me]) if res == 1]
        while wins:
            loser = wins.pop()
            for enemy, res in enumerate(graph[loser]):
                if res == 1 and graph[me][enemy] == 0:
                    graph[me][enemy] = 1
                    graph[enemy][me] = -1
                    wins.append(enemy)
    
    ans = 0
    for row in graph:
        if row.count(0) == 1:
            ans += 1

    return ans