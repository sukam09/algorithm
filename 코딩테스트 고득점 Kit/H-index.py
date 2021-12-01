def solution(citations):
    citations.sort(reverse=True)
    maxval = citations[0]
    for i in range(maxval, -1, -1):
        cnt = 0
        for x in citations:
            if x >= i:
                cnt += 1
            if cnt >= i:
                return i