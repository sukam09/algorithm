def solution(numbers):
    l = [0] * 10
    for n in numbers:
        l[n] = 1
    return sum(i for i, val in enumerate(l) if not val)