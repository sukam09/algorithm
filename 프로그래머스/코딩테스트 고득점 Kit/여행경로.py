from collections import defaultdict, deque

def solution(tickets):
    ans = []
    n = len(tickets)
    dpt = defaultdict(list)
    route = {}
    for i, val in enumerate(tickets):
        dpt[val[0]].append(i)
    for i, val in enumerate(tickets):
        route[i] = dpt[val[1]]
    q = deque()
    for first_dpt in dpt['ICN']:
        q.append([first_dpt])
    while q:
        cur = q.popleft()
        dpt = cur[-1]
        if len(cur)==n:
            ans.append(cur)
        for arv in route[dpt]:
            if arv not in cur:
                q.append(cur+[arv])
    for i in range(len(ans)):
        for j in range(n):
            ans[i][j] = tickets[ans[i][j]][1]
        ans[i] = ['ICN']+ans[i]
    ans = sorted(ans)[0]
    return ans