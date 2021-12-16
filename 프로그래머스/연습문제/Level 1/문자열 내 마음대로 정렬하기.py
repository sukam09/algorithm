def solution(strings, n):
    return sorted(strings, key=lambda s: (s[n], s))

strings = [['sun', 'bed', 'car'], ['abce', 'abcd', 'cdx']]
n = [1, 2]