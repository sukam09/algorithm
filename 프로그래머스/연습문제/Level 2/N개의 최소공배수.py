from functools import reduce

def div(n, arr):
    for i in arr:
        if n % i:
            return False
    return True

def solution(arr):
    maxval = reduce(lambda a, b: a * b, arr)
    for i in range(1, maxval + 1):
        if div(i, arr):
            return i