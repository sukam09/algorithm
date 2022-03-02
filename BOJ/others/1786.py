T = input()
P = input()
lt, lp = len(T), len(P)
table = [0] * lp
j = 0
for i in range(1, lp):
    while j > 0 and P[i] != P[j]:
        j = table[j - 1]
    if P[i] == P[j]:
        j += 1
        table[i] = j
j = 0
ans = []
for i in range(lt):
    while j > 0 and T[i] != P[j]:
        j = table[j - 1]
    if T[i] == P[j]:
        if j == lp - 1:
            ans.append(i - lp + 2)
            j = table[j]
        else:
            j += 1
print(len(ans))
print(*ans)