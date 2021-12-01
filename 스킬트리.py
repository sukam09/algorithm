from collections import deque

def check(skill, skill_tree):
    q = deque(skill)
    for st in skill_tree:
        if st in skill:
            if st == q[0]:
                q.popleft()
            else:
                return 0
    return 1

def solution(skill, skill_trees):
    ans = 0
    
    for skill_tree in skill_trees:
        res = check(skill, skill_tree)
        ans += res
    
    return ans