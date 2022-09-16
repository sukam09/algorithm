m = int(input())
n = int(input())
prime = []

for i in range(m, n + 1):
    if i == 1:
        is_prime = False
    else:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
    
    if is_prime:
        prime.append(i)

if len(prime) > 0:
    print('%d\n%d' % (sum(prime), min(prime)))
else:
    print(-1)