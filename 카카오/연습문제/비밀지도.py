def solution(n, arr1, arr2):
    ans = []
    bin1 = ['0' * (n - len(bin(i)[2:])) + bin(i)[2:] for i in arr1]
    bin2 = ['0' * (n - len(bin(i)[2:])) + bin(i)[2:] for i in arr2]
    for i in range(n):
        res = ''
        for j in range(n):
            res += ' ' if bin1[i][j] == bin2[i][j] == '0' else '#'
        ans.append(res)
    return ans