import sys
input = lambda: sys.stdin.readline().rstrip()
try:
    sys.stdin = open('input.txt', 'r')
except:
    pass

