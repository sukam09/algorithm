# WA 받은 코드 -> 수정 필요
import sys
from collections import defaultdict
input = sys.stdin.readline

# 컨테이너 벨트가 고장났을 경우 경로를 따라가서 최종 위치를 구함
def find(x):
  while True:
    if not broken[x]:
      return x
    x = route[x]

q = int(input())
pos = defaultdict(lambda: -1)  # 컨베이어 벨트의 어디에 위치하는가?
weight = {}
for _ in range(q):
  op = list(map(int, input().split()))
  if op[0] == 100:
    n, m = op[1], op[2]
    cnum = {}  # 몇번 컨베이어 벨트에 속해 있는가?
    broken = [False] * m
    st = [-1] * m  # i번 컨베이어 벨트의 맨 앞 위치
    route = [-1] * m  # i번 컨베이어 벨트가 고장났을 경우 이동한 경로
    dat = [-1] * n
    pre = [-1] * n
    nxt = [-1] * n
    num = 0
    cnt = 0
    for i in range(n):
      if cnt == n // m:
        en = i - 1
        nxt[en] = st[num]
        pre[st[num]] = en
        num += 1
        cnt = 0
      id_, w = op[3 + i], op[3 + i + n]
      pos[id_] = i
      weight[id_] = w
      cnum[id_] = num
      if cnt == 0:
        st[num] = i
        dat[i] = id_
      else:
        dat[i] = id_
        nxt[i - 1] = i
        pre[i] = i - 1
      cnt += 1
    # 마지막 부분 처리
    en = n - 1
    nxt[en] = st[m - 1]
    pre[st[m - 1]] = en
  elif op[0] == 200:
    w_max = op[1]
    s = 0
    for i in range(m):
      if st[i] == -1:
        continue
      w = weight[dat[st[i]]]
      if w <= w_max:
        en = pre[st[i]]
        nxt[en] = nxt[st[i]]
        pre[nxt[st[i]]] = en
        pos[dat[st[i]]] = -1
        st[i] = nxt[st[i]]
        s += w
      else:
        st[i] = nxt[st[i]]
    print(s)
  elif op[0] == 300:
    r_id = op[1]
    if pos[r_id] != -1:
      cur = pos[r_id]
      x = find(cnum[dat[cur]])
      if cur == pre[cur] == nxt[cur]:  # 하나뿐인 경우
        st[x] = -1
      else:
        nxt[pre[cur]] = nxt[cur]
        pre[nxt[cur]] = pre[cur]
        pos[r_id] = -1
        if cur == st[x]:
          st[x] = nxt[cur]
      pos[r_id] = -1
      print(r_id)
    else:
      print(-1)
  elif op[0] == 400:
    f_id = op[1]
    if pos[f_id] != -1:
      cur = pos[f_id]
      x = find(cnum[dat[cur]])
      print(x + 1)
      st[x] = cur
    else:
      print(-1)
  else:
    b_num = op[1] - 1
    if broken[b_num]:
      print(-1)
    else:
      print(b_num + 1)
      broken[b_num] = True
      target = -1
      for i in range(b_num + 1, m):
        if not broken[i]:
          target = i
          break
      else:
        for i in range(m):
          if not broken[i]:
            target = i
            break
      route[b_num] = target
      # b_num 컨베이어가 비어있으면 안옮겨도 됨
      if st[b_num] != -1:
        if st[target] == -1:
          st[target] = st[b_num]
        else:
          en = pre[st[target]]
          ben = pre[st[b_num]]
          nxt[en] = st[b_num]
          pre[st[b_num]] = en
          pre[st[target]] = ben
          nxt[ben] = st[target]
      st[b_num] = -1