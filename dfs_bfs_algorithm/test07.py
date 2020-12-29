from collections import deque
import copy
n = int(input())

board = []
for i in range(n):
    board.append(list(input()))

copy_board = copy.deepcopy(board)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if copy_board[i][j] == 'G':
            copy_board[i][j] = 'R'

def bfs(i,j,array,check_str):
    q = deque()
    q.append([i,j])
    array[i][j] = 0

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<n and 0<=ny<n:
                if array[nx][ny] == check_str:
                    array[nx][ny] = 0
                    q.append([nx,ny])

cnt = 0
copy_cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            bfs(i,j,board,board[i][j])
            cnt += 1
        if copy_board[i][j] != 0:
            bfs(i,j,copy_board,copy_board[i][j])
            copy_cnt += 1

print(cnt, copy_cnt)
