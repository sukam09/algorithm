def solution(N, number):
    if N == number:
        return 1
        
    dp = [set(), set([N])]
    range_checked = lambda x: 1 <= x <= 32000
    
    for i in range(2, 9):
        temp = set([int(str(N) * i)])
        for j in range(1, i // 2 + 1):
            for a in dp[j]:
                for b in dp[i - j]:
                    for res in a + b, a * b, a - b, b - a:
                        if range_checked(res):
                            temp.add(res)
                    
                    if b != 0 and range_checked(a // b):
                        temp.add(a // b)
                    if a != 0 and range_checked(b // a):
                        temp.add(b // a)
                    
                    if number in temp:
                        return i
        
        dp.append(temp)
    
    return -1