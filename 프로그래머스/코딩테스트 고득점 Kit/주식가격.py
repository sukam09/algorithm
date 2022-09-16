def solution(prices):
    ans = [0] * len(prices)
    prices = [(x, y) for x, y in enumerate(prices)]
    S = [prices[0]]
    for x, y in prices[1:]:
        if y >= S[-1][1]: S.append((x, y))
        else:
            while S and S[-1][1] > y:
                idx = S.pop()[0]
                ans[idx] = x - idx
            S.append((x, y))
    while S:
        idx = S.pop()[0]
        ans[idx] = len(prices) - 1 - idx
    return ans