s = input()
bomb = input()
n = len(bomb)
target = list(bomb)

stack = []
for c in s:
    stack.append(c)
    if len(stack) >= n and stack[-n:] == target:
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else "FRULA")