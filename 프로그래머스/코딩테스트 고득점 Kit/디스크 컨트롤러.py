from heapq import heappush, heappop, heapify

def solution(jobs):
    ans = 0
    n = len(jobs)
    heapify(jobs)
    h = []
    running = False
    cnt = 0
    t = 0
    while cnt < n:
        while jobs and jobs[0][0] == t:
            i, j = heappop(jobs)
            heappush(h, (j, i))
        if running and t - start == reqtime:
            ans += t - init
            running = False
            cnt += 1
        if not running and h:
            i, j = heappop(h)
            reqtime, init = i, j
            start = t
            running = True
        t += 1
    return ans // n