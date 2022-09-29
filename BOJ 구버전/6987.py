for _ in range(4):
    L = list(map(int, input().split()))
    

# def likelihood():
#     win, loss = 0, 0
#     draw = []
#     for r in res:
#         w, d, l = r[0], r[1], r[2]
#         if (w == 6 or d == 6 or l == 6) or w + d + l != 5:
#             return 0
#         win += w
#         loss += l
#         draw.append(d)
#     draw.sort(reverse=True)
#     if win != loss or win > 15 or loss > 15 or sum(draw) > 15:
#         return 0
#     dval = 0
#     for d in draw:
#         dval += -d if dval > 0 else d
#     if dval != 0:
#         return 0
#     else:
#         return 1

# ans = []
# for _ in range(4):
#     L = list(map(int, input().split()))
#     res = [[[] for _ in range(3)] for _ in range(6)]
#     for i, val in enumerate(L):
#         res[i // 3][i % 3] = val
#     ans.append(likelihood())
# print(*ans)