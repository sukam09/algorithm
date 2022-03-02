import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers = [str(x) for x in sorted(numbers)]
print('\n'.join(numbers))