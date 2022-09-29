N = input()
if len(N) == 1:
    N = '0' + N
old_N = N
count = 0

while True:
    sum = int(N[0]) + int(N[1])
    N = N[1] + str(sum)[-1]
    count += 1
    if len(N) == 1:
        N = '0' + N
    if N == old_N:
        print(count)
        break
