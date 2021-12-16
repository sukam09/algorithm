def solution(routes):
    routes.sort(key=lambda x: x[1])
    cam = -30001
    ans = 0

    for start, end in routes:
        if start > cam:
            cam = end
            ans += 1
    
    return ans