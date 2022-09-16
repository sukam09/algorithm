from sys import stdin
input = stdin.readline

N = int(input())
word_set = set()

for _ in range(N):
    word_set.add(input().rstrip())

word_set = sorted(list(word_set), key=lambda item: (len(item), item))

for word in word_set:
    print(word)