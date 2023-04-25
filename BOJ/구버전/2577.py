A, B, C = int(input()), int(input()), int(input())
result = str(A * B * C)
digit = [0] * 10
for d in result:
    digit[int(d)] += 1
for i in range(10):
    print(digit[i])
