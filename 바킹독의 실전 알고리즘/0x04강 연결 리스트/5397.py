input = __import__('sys').stdin.readline

def insert(addr, c):
    global unused
    dat[unused] = c
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def erase(addr):
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]

def traversal():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end='')
        cur = nxt[cur]

def solve():
    global dat, pre, nxt, unused
    mx = 1000000
    dat = [-1] * mx
    pre = [-1] * mx
    nxt = [-1] * mx
    unused = 1
    cur = 0
    for c in s:
        if c == '<':
            if pre[cur] != -1:
                cur = pre[cur]
        elif c == '>':
            if nxt[cur] != -1:
                cur = nxt[cur]
        elif c == '-':
            if pre[cur] != -1:
                erase(cur)
                cur = pre[cur]
        else:
            insert(cur, c)
            cur = nxt[cur]
    traversal()
    print()

t = int(input())
for _ in range(t):
    s = input().rstrip()
    solve()