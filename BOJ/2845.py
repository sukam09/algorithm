L, P = map(int, input().split())
participant = list(map(int, input().split()))
for p in participant:
    print(p - L * P, end=' ')