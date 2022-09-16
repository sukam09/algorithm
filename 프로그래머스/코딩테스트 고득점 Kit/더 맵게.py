from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    ans = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            return ans
        i = heappop(scoville)
        j = heappop(scoville)
        new = i + j * 2
        ans += 1
        heappush(scoville, new)
    if scoville[0] >= K:
        return ans
    else:
        return -1