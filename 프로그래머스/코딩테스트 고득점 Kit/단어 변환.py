from collections import defaultdict, deque

def solution(begin, target, words):
    graph = defaultdict(list)
    visited = defaultdict(int)
    times = defaultdict(int)
    q = deque([begin])
    visited[begin] = 1
    words.append(begin)
    l = len(words[0])
    for first in words:
        for second in words:
            if first==second:
                continue
            cnt = 0
            for i in range(l):
                if first[i]!=second[i]:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1:
                graph[first].append(second)
    while q:
        cur = q.popleft()
        t = times[cur]
        for next in graph[cur]:
            if next == target:
                return times[cur] + 1
            if not visited[next]:
                q.append(next)
                visited[next] = 1
                times[next] = t + 1
    return 0