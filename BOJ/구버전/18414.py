x, l, r = map(int, input().split())
if l <= x <= r:
    print(x)
elif x < l:
    print(l)
else:
    print(r)