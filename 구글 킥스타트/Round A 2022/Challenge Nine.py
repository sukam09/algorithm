import sys

input = sys.stdin.readline


def solve(n):
    target = sum(int(x) for x in n)
    step = 0
    while target % 9 != 0:
        target += 1
        step += 1
    idx = len(n)
    for i in range(len(n)):
        if int(n[i]) > step:
            if step == 0 and i == 0:
                continue
            idx = i
            break
    return n[:idx] + str(step) + n[idx:]


t = int(input())
for i in range(1, t + 1):
    n = input().rstrip()
    print(f"Case #{i}: {solve(n)}")
