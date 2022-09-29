p = input()
s = []
for c in p:
    s.append(c)
    try:
        if s[-1]==')':
            if s[-2]=='(':
                for _ in range(2): s.pop()
                s.append(2)
            elif int(s[-2])==s[-2] and s[-3]=='(':
                num = s[-2]
                for _ in range(3): s.pop()
                s.append(2*num)
        elif s[-1]==']':
            if s[-2]=='[':
                for _ in range(2): s.pop()
                s.append(3)
            elif int(s[-2])==s[-2] and s[-3]=='[':
                num = s[-2]
                for _ in range(3): s.pop()
                s.append(3*num)
        if int(s[-1])==s[-1] and int(s[-2])==s[-2]:
            first = s.pop(); second = s.pop()
            s.append(first+second)
    except: pass
try:
    if len(s)==1 and int(s[0])==s[0]: print(s[0])
    else: print(0)
except: print(0)