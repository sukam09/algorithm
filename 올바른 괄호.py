def solution(s):
    val = 0
    for p in s:
        if p == '(':
            val += 1
        else:
            val -= 1
        if val < 0:
            return False
    
    return val == 0