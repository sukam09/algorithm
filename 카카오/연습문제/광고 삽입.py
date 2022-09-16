def conv(time):
    hh, mm, ss = map(int, time.split(':'))
    return hh * 60 * 60 + mm * 60 + ss

def solution(play_time, adv_time, logs):
    play_time = conv(play_time)
    adv_time = conv(adv_time)
    viewer = [0] * (play_time + 1)
    
    for i, time in enumerate(logs):
        start, end = time.split('-')
        start, end = conv(start), conv(end)
        viewer[start] += 1
        viewer[end] -= 1

    for i in range(1, play_time + 1):
        viewer[i] += viewer[i - 1]
    for i in range(1, play_time + 1):
        viewer[i] += viewer[i - 1]

    maxval, ans = viewer[adv_time - 1], 0
    for i in range(adv_time, play_time):
        val = viewer[i] - viewer[i - adv_time]
        if val > maxval:
            maxval = val
            ans = i + 1 - adv_time

    mm, ss = ans // 60, ans % 60
    hh, mm = mm // 60, mm % 60
    return '%s:%s:%s' % (str(hh).zfill(2), str(mm).zfill(2), str(ss).zfill(2))