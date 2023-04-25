input = __import__('sys').stdin.readline
N = int(input())
R = list(map(int, input().split()))

def gcd(a, b):
    if a < b: return gcd(b, a)
    elif b == 0: return a
    else: return gcd(b, a % b)

n = R[0]
for r in R[1:]:
    m = r
    g = gcd(n, m)
    print(str(n // g) + '/' + str(m // g))