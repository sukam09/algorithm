def find(i, n):
    r, c = i // n, i % n
    return r + 1 if c <= r else c + 1

def solution(n, left, right):
    ans = []
    for i in range(left, right + 1):
        ans.append(find(i, n))
    return ans