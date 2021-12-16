def solution(n):
    if n == 1 or n == 2:
        return n
    
    fibo = [0] * (n + 1)
    fibo[1], fibo[2] = 1, 2
    
    for i in range(3, n + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1000000007
    
    return fibo[n]