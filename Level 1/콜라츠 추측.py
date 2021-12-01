def solution(num):
    ans = 0
    while num != 1:
        if ans == 500:
            return -1
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        ans += 1
    return ans