import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    
    ps = ['(', ')', '[', ']']
    vps = ['()', '[]']
    string = [s for s in string if s in ps]
    string = ''.join(string)

    while vps[0] in string or vps[1] in string:
        string = string.replace(vps[0], '')
        string = string.replace(vps[1], '')
    if string == '':
        print("yes")
    else:
        print("no")