from sys import stdin
from itertools import combinations
input = stdin.readline

n = int(input())
ans = []

# 0 ~ 9로 만들 수 있는 1 ~ 10자리 숫자를 모두 만든 다음 내림차순으로 정렬해서 ans에 저장
# 마지막에 ans를 다시 오름차순으로 정렬
for i in range(1, 11):
    for comb in combinations(range(10), i):
        res = sorted(comb, reverse=True)
        ans.append(int(''.join(map(str, res))))
ans.sort()

try:
    print(ans[n])
except:
    print(-1)