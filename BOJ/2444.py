input = __import__('sys').stdin.readline
N = int(input())
s = ['*' * (2*i+1) for i in range(N)]
for c in s: print(c.center(2*N-1, ' ').rstrip())
for c in s[-2::-1]: print(c.center(2*N-1, ' ').rstrip())