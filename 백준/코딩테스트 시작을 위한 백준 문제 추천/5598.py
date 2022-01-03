s = input()
for c in s:
    idx = ord(c) - ord('A')
    print(chr(ord('A') + (idx - 3) % 26), end='')