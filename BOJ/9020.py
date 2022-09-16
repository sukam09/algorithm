import sys
import math

def prime_check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    partition = []

    for i in range(n // 2, 1, -1):
        if prime_check(i) and prime_check(n - i):
            print(i, n - i)
            break