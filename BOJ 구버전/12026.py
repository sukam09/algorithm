N = int(input())
blocks = list(input())
energy = [-1] * N
b = []
o = []
j = []
for i, block in enumerate(blocks):
    if block == 'B':
        b.append(i)
    elif block == 'O':
        o.append(i)
    else:
        j.append(i)
energy[0] = 0
for i in range(1, N):
    try:
        if blocks[i] == 'B':
            energy[i] = min([energy[tar] + (i - tar) ** 2 for tar in j if tar < i if energy[tar] != -1])
        elif blocks[i] == 'O':
            energy[i] = min([energy[tar] + (i - tar) ** 2 for tar in b if tar < i if energy[tar] != -1])
        else:
            energy[i] = min([energy[tar] + (i - tar) ** 2 for tar in o if tar < i if energy[tar] != -1])
    except:
        pass
print(energy[N - 1])