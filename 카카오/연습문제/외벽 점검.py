from itertools import permutations


def solution(n, weak, dist):
    wl = len(weak)
    
    for i in range(wl):
        weak.append(n + weak[i])

    ans = len(dist) + 1
    cand = list(permutations(dist, len(dist)))

    for i in range(wl):
        start = [weak[j] for j in range(i, i + wl)]
        
        for order in cand:
            fidx, fcnt = 0, 1
            checked_len = start[0] + order[0]
            
            for idx in range(wl):
                if start[idx] > checked_len:
                    fcnt += 1

                    if fcnt > len(order):
                        break

                    fidx += 1
                    checked_len = start[idx] + order[fidx]
            
            ans = min(ans, fcnt)
    
    return -1 if ans > len(dist) else ans