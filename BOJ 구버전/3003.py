piece = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
for p, c in zip(piece, chess):
    print(c - p, end=' ')