m, n = map(int, input().split())
seq = []
num, count = 1, 1
for _ in range(n):
    seq.append(num)
    count -= 1
    if count == 0:
        num += 1
        count = num
print(sum(seq[m - 1:n]))
    
    