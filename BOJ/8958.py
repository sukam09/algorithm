N = int(input())
results = [input() for _ in range(N)]
scores = []

for result in results:
    score, count = 0, 0
    for r in result:
        if r == 'O':
            count += 1
            score += count
        else:
            count = 0
    scores.append(score)

for score in scores:
    print(score)