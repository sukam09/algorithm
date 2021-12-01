def rank(ans):
    return 7 - ans if ans >= 2 else 6

def solution(lottos, win_nums):
    cnt = 0
    unknown = 0
    answer = [False] * 46
    for w in win_nums:
        answer[w] = True
    for l in lottos:
        if answer[l]:
            cnt += 1
        if l == 0:
            unknown += 1
    return [rank(cnt + unknown), rank(cnt)]