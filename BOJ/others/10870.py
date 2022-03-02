import sys

def fibo(n):
    return fibo(n - 1) + fibo(n - 2) if n >= 2 else n

n = int(sys.stdin.readline())
print(fibo(n))