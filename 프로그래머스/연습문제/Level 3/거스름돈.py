def solution(n, money):
    dp = [1] + [0] * n

    # dp[j]는 money[:i + 1]를 이용해서 금액 j를 만드는 경우의 수.
    # i-step에서 dp[j - i]의 가짓수에 동전 i를 더하면 금액 j가 되므로 이를 누적해서 더해 줌.
    for i in money:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    
    # 내가 처음 생각했던 풀이
    # dp[i]는 금액 i를 만드는 경우의 수
    # i-step마다 i >= j인 동전 j에 대하여 금액 i - j를 만드는 경우의 수에 동전 j만 얹으면 같은 경우이므로
    # 위 조건을 만족하는 모든 dp[i - j] 값을 누적
    # 그러나 이렇게 하면 1 + 2 = 3과 2 + 1 = 3이 다른 경우로 취급되어 원래 풀이보다 dp 값이 훨씬 크게 나오는 문제가 발생한다.
    for i in range(1, n + 1):
        for j in money:
            if i >= j:
                dp[i] += dp[i - j]
    
    return dp[n]

print(solution(5, [1, 2, 5]))  # 4