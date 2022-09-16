input = __import__('sys').stdin.readline
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def t2m(s):
    h, m = map(int, s.split(':'))
    return 60 * h + m

s, e, q = input().split()
enter = set()
leave = set()
member = set()
while True:
    try:
        op = input().split()
        if op[1] not in member:
            member.add(op[1])
        op[0] = t2m(op[0])
        if op[0] <= t2m(s):
            enter.add(op[1])
        elif t2m(e) <= op[0] <= t2m(q):
            leave.add(op[1])
    except:
        break
print(len([x for x in member if x in enter if x in leave]))