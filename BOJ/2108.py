import sys
from collections import Counter

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

avg = round(sum(num) / len(num))
mid = sorted(num)[len(num) // 2]
mc = Counter(num).most_common()
mc_max = mc[0][1]
mc_max_list = [(x, y) for x, y in mc if y == mc_max]
if len(mc_max_list) == 1:
    mc_value = mc_max_list[0][0]
else:
    mc_value = sorted(mc_max_list, key=lambda x: x[0])[1][0]

_range = max(num) - min(num)

print(avg)
print(mid)
print(mc_value)
print(_range)
