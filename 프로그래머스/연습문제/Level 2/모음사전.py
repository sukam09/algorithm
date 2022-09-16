from itertools import product

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        for p in product(vowel, repeat=i):
            dictionary.append(''.join(p))

    return sorted(dictionary).index(word) + 1