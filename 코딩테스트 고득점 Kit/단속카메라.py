# TLE
def solution(routes):
    ans = 0
    routes = {tuple(x): 1 for x in routes}
    minval, maxval = -30000, 30000
    while routes:
        res = []
        points = []
        for x in routes:
            for y in x:
                points.append(y) 
        minval, maxval = min(points), max(points)
        for i in range(minval, maxval + 1):
            temp = []
            for j in routes:
                if j[0] <= i <= j[1]:
                    temp.append(j)
            if len(temp) > len(res):
                res = temp
        for x in res:
            del routes[x]
        ans += 1
    return ans