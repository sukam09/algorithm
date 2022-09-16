from itertools import product
from collections import defaultdict

def search(user_id, bid):
    uid = [uid for uid in user_id if len(uid) == len(bid)]
    candidate = []
    for u in uid:
        res = match(u, bid)
        if res:
            candidate.append(u)
    return candidate

def match(u, bid):
    for c, b in zip(u, bid):
        if b != '*' and c != b:
            return False
    return True

def solution(user_id, banned_id):
    case = []
    for bid in banned_id:
        case.append(search(user_id, bid))

    ans = []
    vis = defaultdict(int)
    
    for p in product(*case):
        target = frozenset(p)
        if not vis[target] and len(target) == len(banned_id):
            ans.append(target)
            vis[target] = 1

    return len(ans)