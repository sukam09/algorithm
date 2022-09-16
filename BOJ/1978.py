N = int(input())
num_list = list(map(int, input().split()))
result = 0
for n in num_list:
    if n == 1:
        prime = 0
    else:
        prime = 1    
        for i in range(2, n):
            if n % i == 0:
                prime = 0
                break
    result += prime
print(result)
