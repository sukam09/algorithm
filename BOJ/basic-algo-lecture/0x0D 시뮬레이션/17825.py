from sys import stdin
input = stdin.readline

def sim(idx, tot, locs):
    global ans
    
    if idx == 10:
        ans = max(ans, tot)
        return
    
    dice = dices[idx]

    for i, loc in enumerate(locs):
        if loc == 32:
            continue

        for j in range(dice):
            if loc == 32:
                break
            if j == 0 and loc in special:
                loc = special[loc]
            else:
                loc = nxt[loc]
        
        if loc != 32 and loc in locs:
            continue
        
        tmp = locs[i]
        locs[i] = loc
        sim(idx + 1, tot + scores[loc], locs)
        locs[i] = tmp

dices = list(map(int, input().split()))
locs = [0] * 4
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 30, 35, 22, 24, 28, 27, 26, 0]
special = {5: 21, 10: 27, 15: 29}

nxt = [i + 1 for i in range(32)]
nxt[20] = 32
nxt[26] = 20
nxt[28] = 24
nxt[31] = 24

ans = 0
sim(0, 0, locs)
print(ans)