import sys

N, M = map(int, sys.stdin.readline().split())
board = []
b_chess_board = ('BWBWBWBW' + 'WBWBWBWB') * 4
w_chess_board = ('WBWBWBWB' + 'BWBWBWBW') * 4

# input board
for _ in range(N):
    row = sys.stdin.readline().rstrip()
    board.append(row)

# slicing
ans = []
for i in range(N - 7):
    for j in range(M - 7):
        new_board = [x[j:j + 8] for x in board[i:i + 8]]
        new_board = ''.join(new_board)
        b_ans = [1 for x, y in zip(new_board, b_chess_board) if x != y]
        w_ans = [1 for x, y in zip(new_board, w_chess_board) if x != y]
        ans.append(len(b_ans))
        ans.append(len(w_ans))

print(min(ans))
