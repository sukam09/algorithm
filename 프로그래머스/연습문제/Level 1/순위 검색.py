from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    db = defaultdict(list)
    for i in info:
        i = i.split()
        lan = [i[0], '-']
        job = [i[1], '-']
        career = [i[2], '-']
        soulfood = [i[3], '-']
        score = int(i[4])
        for p in product(lan, job, career, soulfood):
            db[''.join(p)].append(score)
    
    for k in db:
        db[k].sort()
    
    ans = []
    for q in query:
        q = q.split(' and ')
        q[3] = q[3].split()
        x = int(q[3][1])
        tar = q[0] + q[1] + q[2] + q[3][0]
        idx = bisect_left(db[tar], x)
        ans.append(len(db[tar]) - idx)
    
    return ans