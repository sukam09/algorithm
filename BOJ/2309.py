from itertools import combinations
import copy


height = [int(input()) for _ in range(9)]
prohibited = list(combinations(height, 2))
for x in prohibited:
    new_height = copy.deepcopy(height)
    new_height.remove(x[0])
    new_height.remove(x[1])
    if sum(new_height) == 100:
        for x in sorted(new_height):
            print(x)
        break
