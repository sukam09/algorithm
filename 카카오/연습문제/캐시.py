from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cache = {}
    ans = 0
    for i, c in enumerate(cities):
        c = c.lower()
        if c in cache:
            ans += 1
        else:
            if len(cache) == cacheSize:
                tar = [k for k, v in cache.items() if v == min(cache.values())][0]
                del cache[tar]
            ans += 5
        cache[c] = i
    return ans