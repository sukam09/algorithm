import sys

X = int(sys.stdin.readline())
end, step, prev = 1, 1, 0

while end < X:
	prev = end
	step += 1
	end += step

i = X - prev
j = step + 1 - i
if step % 2 == 1:
	i, j = j, i
print('%d/%d' % (i, j))
