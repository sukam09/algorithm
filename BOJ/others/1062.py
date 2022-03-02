from sys import stdin
from itertools import combinations
input = stdin.readline

n, k = map(int, input().split())
words = [input() for _ in range(n)]

if k < 5:
    print(0)
else:
    new_words = []
    for word in words:
        word = [w for w in word if w not in 'acint']
        new_words.append(set(word))
 
    ans = 0
    alpha = 'bdefghjklmopqrsuvwxyz'
    
    for combi in combinations(alpha, k - 5):
        cnt = 0
        combi = set(combi)
        for new_word in new_words:
            if new_word & combi == new_word:
                cnt += 1
        ans = max(cnt, ans)
    
    print(ans)