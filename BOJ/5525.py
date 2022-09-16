n = int(input())
m = int(input())
s = input()

# 'I'가 있는 모든 위치를 memoization
stack = [i for i, c in enumerate(s) if c == 'I']
cnt = 0
ans = 0

"""
시간 복잡도 O(mn)으로 code를 짜면 small case만 통과 가능하지만 다음과 같이 시간 복잡도 O(m)으로 code를 짜면
large case까지 통과 가능함
"""
for i in range(1, len(stack)):
    # 'I'와 'O'만 존재하므로 'I'의 idx 차이가 2가 날 경우 stack[i - 2:i + 1] = 'IOI'
    if stack[i] - stack[i - 1] == 2:
        cnt += 1
    
    # 'IOI'의 패턴이 연속적이지 않은 경우 cnt를 초기화
    else:
        cnt = 0
    
    # 'IOI'의 개수가 n인 경우는 Pn의 패턴이 처음 나온 경우
    # 'IOI'의 개수 > n인 경우는 Pn의 패턴이 끊기지 않고 연속적으로 이어지는 경우
    if cnt >= n:
        ans += 1

print(ans)