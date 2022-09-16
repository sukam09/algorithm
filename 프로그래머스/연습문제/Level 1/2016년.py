def solution(a, b):
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dow = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    cnt = 0
    for i in range(1, a):
        cnt += day[i]
    cnt += b - 1
    return dow[cnt % 7]