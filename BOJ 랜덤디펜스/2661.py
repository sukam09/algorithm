import sys
input = sys.stdin.readline

def dfs(idx):
    if idx == n:
        print(''.join(ans))
        sys.exit(0)
    for i in range(1, 4):
        ans.append(str(i))
        if chk(ans):
            dfs(idx + 1)
        ans.pop()

# 좋은 수열인지 확인
def chk(ans):
    # k는 부분 수열의 길이
    for k in range(1, len(ans) // 2 + 1):
        for i in range(len(ans) - k):
            if ans[i:i + k] == ans[i + k:i + 2*k]:
                return 0
    return 1

n = int(input())
ans = []
dfs(0)