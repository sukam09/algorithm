import sys

L = int(sys.stdin.readline())
string = [ord(x) - ord('a') + 1 for x in sys.stdin.readline().rstrip()]
string = [value * 31 ** i for i, value in enumerate(string)]
print(sum(string) % 1234567891)