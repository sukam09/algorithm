from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
y, m = 0, 0
for x in arr:
    y += (x // 30 + 1) * 10
    m += (x // 60 + 1) * 15

if y < m:
    fare = "Y"
elif m < y:
    fare = "M"
else:
    fare = "Y M"
    
print(fare, min(y, m))