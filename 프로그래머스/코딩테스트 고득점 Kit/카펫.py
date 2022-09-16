from math import sqrt

def solution(brown, yellow):
    divisor = []
    for i in range(1, int(sqrt(yellow))+1):
        if yellow % i == 0:
            divisor.append(i)
    for x in divisor:
        y = yellow // x
        if (y + 2) * (x + 2) - y * x == brown:
            return [y + 2, x + 2]