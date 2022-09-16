def gcd(n, m):
    if n < m:
        n, m = m, n
    while m:
        n, m = m, n % m
    return n

def solution(n, m):
    gcdval = gcd(n, m)
    return [gcdval, gcdval * (n // gcdval) * (m // gcdval)]