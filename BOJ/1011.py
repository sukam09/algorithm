'''
1(1 ** 2): 1 -> 1
2: 1 1 -> 2 -> 1 + 1
3: 1 1 1 -> 3
4(2 ** 2): 1 2 1 -> 3
5: 1 2 1 1 -> 4 -> 
6: 1 2 2 1 -> 4 -> 4 + 2(max)
7: 1 2 2 1 1 -> 5
9(3 ** 2): 1 2 3 2 1 -> 5
10: 1 2 3 2 1 1 -> 6
11: 1 2 3 2 2 1 -> 6
12: 1 2 3 3 2 1 -> 6
13: 1 2 3 3 2 1 1 -> 7
14: 1 2 3 3 2 2 1 -> 7
15: 1 2 3 3 3 2 1 -> 7
16(4 ** 2): 1 2 3 4 3 2 1 -> 7
17: 1 2 3 4 3 2 1 1 -> 8 -> 16 + 1
18: 1 2 3 4 3 2 2 1 -> 8 -> 16 + 2
19: 1 2 3 4 3 3 2 1 -> 8 -> 16 + 3
20: 1 2 3 4 4 3 2 1 -> 8 -> 16 + 4(max)
21: 1 2 3 4 4 3 2 1 1 -> 9 
25(5 ** 2): 1 2 3 4 5 4 3 2 1 -> 9

if n == k ** 2 -> 2 * k - 1
if n == k ** 2 + 1 -> 2 * k
'''

import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x
    for i in range(dist, 0, -1):
        if math.sqrt(i) == int(math.sqrt(i)):
            square = i
            target = int(math.sqrt(i))
            break
    ans = 2 * target - 1

    if dist - square > target:
        ans += 2
    elif dist - square > 0:
        ans += 1
    print(ans)
