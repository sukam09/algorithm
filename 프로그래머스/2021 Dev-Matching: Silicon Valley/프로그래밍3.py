from collections import deque
from math import gcd

def powersum(w):
    if len(set(w)) == 1:
        return 0
    return sum(x ** 2 for x in w)

def wavesum(w1, w2):
    ws = []
    l1, l2 = len(w1), len(w2)
    wavelen = gcd(l1, l2) * (l1 // gcd(l1, l2)) * (l2 // gcd(l1, l2))
    w1 = w1 * (wavelen // len(w1)) + w1 * (wavelen % len(w1))
    w2 = w2 * (wavelen // len(w2)) + w1 * (wavelen % len(w2))

    for i in range(len(ws), 0, -1):
        if len(ws) % i == 0 and ws[:len(ws) // i] * i == ws:
            return ws[:len(ws) // i]

def solution(wave1, wave2):
    wave1 = deque(wave1)
    wave2 = deque(wave2)
    ans = float('inf')

    for i in range(len(wave1)):
        wave1.rotate()
        for j in range(len(wave2)):
            wave2.rotate()
            ws = wavesum(wave1, wave2)
            ps = powersum(ws)
            ans = min(ans, ps)
    
    return ans