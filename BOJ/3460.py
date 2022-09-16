t = int(input())
for _ in range(t):
    n = int(input())
    for i, c in enumerate(bin(n)[2:][::-1]):
        if c == '1':
            print(i, end=' ')
    print()