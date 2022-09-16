import sys
input = sys.stdin.readline

def run(x):
    cur = x
    while True:
        state[cur] = x
        cur = arr[cur]
        if state[cur] == x:
            while state[cur] != -1:
                state[cur] = -1
                cur = arr[cur]
            return
        elif state[cur] != 0:
            return

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    state = [0] * (n + 1)
    for i in range(1,  n + 1):
        if state[i] == 0:
            run(i)
    print(n - state.count(-1))