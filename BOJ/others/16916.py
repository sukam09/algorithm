def kmp():
    j = 0
    for i in range(ls):
        while j > 0 and S[i] != P[j]:
            j = table[j - 1]
        if S[i] == P[j]:
            if j == lp - 1:
                return 1
            else:
                j += 1
    return 0

S = input()
P = input()
ls, lp = len(S), len(P)
table = [0] * lp
j = 0
for i in range(1, lp):
    while j > 0 and P[i] != P[j]:
        j = table[j - 1]
    if P[i] == P[j]:
        j += 1
        table[i] = j
print(kmp())