def get_priority(n):
    n = str(n)
    if n == '0':
        return -1
    elif n == '1000':
        return 0
    elif len(n) == 3:
        return int(n) * 10
    elif len(n) == 1:
        return int(n * 3) * 10
    else:
        if n[0] > n[1]:
            return int(n + n[0]) * 10 - 5
        if n[0] == n[1]:
            return int(n + n[0]) * 10
        else:
            return int(n + n[0]) * 10 + 5

def solution(numbers):
    numbers.sort(key=get_priority, reverse=True)
    ans = ''.join(map(str, numbers))
    return '0' if ans.count('0') == len(ans) else ans