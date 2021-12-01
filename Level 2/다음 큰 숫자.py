def solution(n):
    ans = n + 1
    while bin(ans).count('1') != bin(n).count('1'):
        ans += 1
    return ans