def solution(arr):
    ans = []
    cur = -1
    for i in arr:
        if i != cur:
            ans.append(i)
            cur = i
    return ans