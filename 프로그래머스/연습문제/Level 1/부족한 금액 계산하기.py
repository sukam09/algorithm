def solution(price, money, count):
    cur = 0
    for i in range(1, count + 1):
        cur += price * i
    return cur - money if cur >= money else 0