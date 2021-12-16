def solution(number, k):
    number = list(number)
    ans = []
    for x in number:
        while k and ans and ans[-1] < x:
            ans.pop()
            k -= 1
        ans.append(x)
    while k:
        ans.pop()
        k -= 1
    ans = ''.join(ans)
    return ans