def solution(s):
    ntoa = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    aton = {k: v for v, k in ntoa.items()}
    for i in range(10):
        s = s.replace(ntoa[i], str(aton[ntoa[i]]))
    return int(s)