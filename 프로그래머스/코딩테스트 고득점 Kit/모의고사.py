def solution(answers):
    L = len(answers)
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans1 = A * (L // 5) + A[:L % 5]
    ans2 = B * (L // 8) + B[:L % 8]
    ans3 = C * (L // 10) + C[:L % 10]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i, j, k, l in zip(answers, ans1, ans2, ans3):
        if j == i:
            cnt1 += 1
        if k == i:
            cnt2 += 1
        if l == i:
            cnt3 += 1
    maxval = max(cnt1, cnt2, cnt3)
    ans = [(1, cnt1), (2, cnt2), (3, cnt3)]
    ans = [x for x, y in ans if y == maxval]
    return ans