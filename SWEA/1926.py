n = int(input())
for i in range(1, n + 1):
    num = i
    clap = 0
    while num:
        digit = num % 10
        if digit and digit % 3 == 0:
            clap += 1
        num //= 10
        
    print("-" * clap, end=' ') if clap else print(i, end=' ')