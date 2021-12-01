def convtomel(ms):
    melody = []
    sharp = False
    for i in range(len(ms)):
        if sharp:
            sharp = False
            continue
        if ms[i] == 'E' or ms[i] == 'B':
            melody.append(ms[i])
        elif i < len(ms) - 1 and ms[i + 1] == '#':
            melody.append(ms[i:i + 2])
            sharp = True
        else:
            melody.append(ms[i])
    return melody

def solution(m, musicinfos):
    start, end, title, musicscore = [], [], [], []
    musiclen = []

    for mi in musicinfos:
        s, e, t, ms = mi.split(',')
        start.append(s)
        end.append(e)
        title.append(t)
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        
        melody = convtomel(ms)
        ml = (eh - sh) * 60 + em - sm
        musiclen.append(ml)
        ml += len(m) - 1
        ms = melody * (ml // len(melody)) + melody[:ml % len(melody)]
        musicscore.append(ms)

    res = []
    m = convtomel(m)
    for i, ms in enumerate(musicscore):
        for j in range(len(ms) - (len(m) - 1)):
            if m == ms[j:j + len(m)]:
                res.append((title[i], musiclen[i]))
                break
    
    if res:
        return sorted(res, key=lambda item: -item[1])[0][0]
    else:
        return '(None)'