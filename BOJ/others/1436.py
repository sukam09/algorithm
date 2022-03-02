input = __import__('sys').stdin.readline
N = int(input())
title = 0
cnt = 0
for i in range(666, 2666800):
    if '666' in str(i):
        title = i
        cnt += 1
        if cnt == N:
            print(title)
            break