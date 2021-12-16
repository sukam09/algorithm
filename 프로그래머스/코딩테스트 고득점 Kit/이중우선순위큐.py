from heapq import heappush, heappop

def reverse(h, imode):
    rh = []
    while h:
        m, n = heappop(h)
        heappush(rh, (n, m))
    imode = not imode
    return rh, imode

def solution(operations):
    h = []
    imode = False
    for x in operations:
        c, i = x.split()
        i = int(i)
        if c == 'I':
            if imode:
                heappush(h, (-i, i))
            else:
                heappush(h, (i, -i))
        elif h:
            if i == -1:
                if imode:
                    h, imode = reverse(h, imode)
                heappop(h)
            else:
                if not imode:
                    h, imode = reverse(h, imode)
                heappop(h)
    if h:
        if not imode:
            h, imode = reverse(h, imode)
        maxval = h[0][1]
        h, imode = reverse(h, imode)
        minval = h[0][0]
        ans = [maxval, minval]
    else:
        ans = [0, 0]
    return ans