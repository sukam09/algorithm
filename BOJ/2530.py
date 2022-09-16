a, b, c = map(int, input().split())
d = int(input())
time = a * 60 * 60 + b * 60 + c + d
ss = time % 60
hh = time // 60 // 60 % 24
mm = time // 60 % 60
print(hh, mm, ss)