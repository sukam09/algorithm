from sys import stdin
from itertools import product
input = stdin.readline

def is_duplicated(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

s = input()
cand = []  # 각 자리에 들어갈 수 있는 모든 번호의 set을 들고 있는 list
chrset = 'abcdefghijklmnopqrstuvwxyz'
numset = range(10)

for c in s:
    if c == 'c':
        cand.append(chrset)
    else:
        cand.append(numset)

if len(s) == 1:
    print(len(cand[0]))
else:
    ans = 0
    # cand에 있는 set으로 cartesian product를 구한 뒤에 두 자리 연속으로 중복되는 경우를 제외하고 count
    for p in product(*cand):
        if not is_duplicated(p):
            ans += 1
    print(ans)