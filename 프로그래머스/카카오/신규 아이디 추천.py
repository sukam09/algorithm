def solution(new_id):
    new_id = new_id.lower()
    bans = '~!@#$%^&*()=+[{]}:?,<>/'

    for ban in bans:
        new_id = new_id.replace(ban, '')
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    s = ''
    for i, c in enumerate(new_id):
        if i == 0 and c == '.':
            continue
        if i == len(new_id) - 1 and c == '.':
            continue
        s += c
    new_id = s

    if not new_id:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id