from math import gcd

def solution(w, h):
    n = gcd(w, h)
    origin = w * h
    w, h = w // n, h // n
    return origin - (w + h - 1) * n