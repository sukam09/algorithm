formula = input()
s = []
new_s = []
cur = 0
for i, c in enumerate(formula):
    if c == '+' or c == '-':
        s.append(formula[cur:i])
        s.append(formula[i])
        cur = i + 1
s.append(formula[cur:])
for c in s:
    try:
        new_s.append(int(c))
    except:
        new_s.append(c)
    if len(new_s) >= 2 and new_s[-2] == '+':
        second = new_s.pop()
        plus = new_s.pop()
        first = new_s.pop()
        new_s.append(first + second)
print(eval(''.join(map(str, new_s))))