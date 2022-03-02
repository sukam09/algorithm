from itertools import permutations
input = __import__('sys').stdin.readline
N = int(input())
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
operator = '+' * plus + '-' * minus + '*' * mul + '/' * div
operator = list(operator)
p = set(permutations(operator))
ans = [None] * len(p)
for idx, x in enumerate(p):
    res = A[0]
    for i in range(N - 1):
        cur = A[i + 1]
        if x[i] == '+': res += cur
        elif x[i] == '-': res -= cur
        elif x[i] == '*': res *= cur
        else:
            if res < 0: res = -(-res // cur)
            else: res = res // cur
    ans[idx] = res
print(max(ans))
print(min(ans))