def solution(arr1, arr2):
    a, b = len(arr1), len(arr2[0])
    c = len(arr1[0])
    ans = [[0] * b for _ in range(a)]
    
    for i in range(a):
        for j in range(b):
            for k in range(c):
                ans[i][j] += arr1[i][k] * arr2[k][j]
    
    return ans