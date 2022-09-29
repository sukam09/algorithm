from collections import Counter

vocab = input().split()
counter = Counter(vocab)
count_list = list(counter.values())
print(sum(count_list))
