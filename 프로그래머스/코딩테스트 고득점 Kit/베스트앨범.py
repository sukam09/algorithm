from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(dict)
    for i in range(len(genres)):
        try:
            dic[genres[i]][plays[i]].append(i)
        except:
            dic[genres[i]][plays[i]] = [i]
    genres_cnt = [(x, sum(dic[x].keys())) for x in dic]
    genres_cnt.sort(key=lambda x: -x[1])
    ans = []
    for x in genres_cnt:
        plays_cnt = sorted(list(dic[x[0]].items()), key=lambda x: -x[0])
        lim = 2
        for y in plays_cnt:
            if lim:
                if len(y[1]) == 1:
                    ans.append(y[1][0])
                else:
                    ans.append(y[1][0])
                    ans.append(y[1][1])
                lim -= len(y[1])
            else:
                break
    return ans