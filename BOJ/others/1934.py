input = __import__('sys').stdin.readline
T = int(input())

def gcd(A, B):
    if B == 0: return A
    else: return gcd(min(A, B), max(A, B) % min(A, B))

for _ in range(T):
    A, B = map(int, input().split())
    print(gcd(A, B) * (A // gcd(A, B) * (B // gcd(A, B))))