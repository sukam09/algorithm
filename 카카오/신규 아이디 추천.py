def solution(new_id):
    banned = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = new_id.lower()
    for c in banned:
        new_id = new_id.replace(c , '')
    
    new_id = list(new_id)
    point = False
    for i, c in enumerate(new_id):
        if point:
            if c == '.':
                new_id[i] = ''
            else:
                point = False
        if not point and c == '.':
            point = True
    
    new_id = list(''.join(new_id))
    if new_id:
        if new_id[0] == '.':
            new_id[0] = ''
        if new_id[-1] == '.':
            new_id[-1] = ''
        new_id = list(''.join(new_id))
    if not new_id:
        new_id = ['a']
    
    new_id = list(''.join(new_id))
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id.pop()
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    
    ans = ''.join(new_id)
    return ans