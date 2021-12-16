def solution(gems):
    n = len(gems)
    gem_type = len(set(gems))
    
    l, r = 0, 0
    gem_counter = {}
    minval = n
    ans = [1, n]

    while l < n:
        if r < n and len(gem_counter) < gem_type:
            if gems[r] not in gem_counter:
                gem_counter[gems[r]] = 1
            else:
                gem_counter[gems[r]] += 1
            r += 1
        else:
            if len(gem_counter) == gem_type and r - l < minval:
                minval = r - l
                ans = [l + 1, r]

            gem_counter[gems[l]] -= 1
            if gem_counter[gems[l]] == 0:
                del gem_counter[gems[l]]
            l += 1
    
    return ans