input = __import__('sys').stdin.readline

def pow(a, b, c):
    if b == 1:
        return a % c
    val = pow(a, b // 2, c)
    val = val * val % c
    return val if b % 2 == 0 else val * a % c

a, b, c = map(int, input().split())
print(pow(a, b, c))