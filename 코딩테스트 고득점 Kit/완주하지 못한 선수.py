from collections import Counter

def solution(participant, completion):
    P = Counter(participant)
    C = Counter(completion)
    for x in P:
        try:
            if P[x] != C[x]:
                return x
        except:
            return x