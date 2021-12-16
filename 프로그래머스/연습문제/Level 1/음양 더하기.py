def solution(absolutes, signs):
    ans = 0
    for a, s in zip(absolutes, signs):
        ans += a if s else -a
    return ans