def solution(arr1, arr2):
    r, c = len(arr1), len(arr1[0])
    ans = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            ans[i][j] = arr1[i][j] + arr2[i][j]
    return ans