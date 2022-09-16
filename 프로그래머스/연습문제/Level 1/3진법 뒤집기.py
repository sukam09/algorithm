def solution(n):
    ans = 0
    ternary = []
    while n:
        ternary.append(n % 3)
        n //= 3
    for t in ternary:
        ans = ans * 3 + t
    return ans