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

s = input().rstrip()
m = int(input())
mx = 1000000
dat = [-1] * mx
pre = [-1] * mx
nxt = [-1] * mx
unused = 1
cur = 0
for c in s:
    insert(cur, c)
    cur = nxt[cur]
for _ in range(m):
    op = input().split()
    if len(op) == 2:
        insert(cur, op[1])
        cur = nxt[cur]
    elif op[0] == 'L':
        if pre[cur] != -1:
            cur = pre[cur]
    elif op[0] == 'D':
        if nxt[cur] != -1:
            cur = nxt[cur]
    else:
        if pre[cur] != -1:
            erase(cur)
            cur = pre[cur]
traversal()