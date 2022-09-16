def solution(array, commands):
    ans = []
    for c in commands:
        i, j, k = c
        res = sorted(array[i - 1:j])[k - 1]
        ans.append(res)
    return ans