n = int(input())
words = [input() for _ in range(n)]
words.sort()

ans = 1
for i in range(1, n):
    if not words[i].startswith(words[i - 1]):
        ans += 1

print(ans)