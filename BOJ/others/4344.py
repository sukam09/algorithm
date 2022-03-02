C = int(input())
input_list = [list(map(int, input().split())) for _ in range(C)]
for x in input_list:
    N, scores = x[0], x[1:]
    avg = sum(scores) / N
    above_avg = 0
    for y in scores:
        if y > avg:
            above_avg += 1
    above_avg_rate = above_avg / N * 100
    print('%.3f%%' % above_avg_rate)
