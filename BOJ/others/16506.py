def preprocess(x):
    try:
        return int(x)
    except:
        return x

def pad(x, n):
    while len(x) < n:
        x = '0' + x
    return x

N = int(input())
operation = {
    'ADD': '00000',
    'ADDC': '00001',
    'SUB': '00010',
    'SUBC': '00011',
    'MOV': '00100',
    'MOVC': '00101',
    'AND': '00110',
    'ANDC': '00111',
    'OR': '01000',
    'ORC': '01001',
    'NOT': '01010',
    'MULT': '01100',
    'MULTC': '01101',
    'LSFTL': '01110',
    'LSFTLC': '01111',
    'LSFTR': '10000',
    'LSFTRC': '10001',
    'ASFTR': '10010',
    'ASFTRC': '10011',
    'RL': '10100',
    'RLC': '10101',
    'RR': '10110',
    'RRC': '10111'
}

for _ in range(N):
    opcode, rD, rA, rB = map(preprocess, input().split())
    ans = operation[opcode] + '0' + pad(bin(rD)[2:], 3) + pad(bin(rA)[2:], 3)\
        + (pad(bin(rB)[2:], 4) if opcode[-1] == 'C' else pad(bin(rB)[2:], 3) + '0')
    print(ans)