from collections import deque
import sys
n,l,r = map(int, sys.stdin.readline().rstrip().split())

board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def process(x,y,index):
    untitled = []
    untitled.append([x,y])
    visit[x][y] = index
    cnt = 1
    summary = board[x][y]
    
    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if l <= abs(board[x][y] - board[nx][ny]) <= r and visit[nx][ny] == -1:
                    q.append([nx,ny])
                    untitled.append([nx,ny])
                    cnt += 1
                    summary += board[nx][ny]
                    visit[nx][ny] = index
    
    for ux,uy in untitled:    
        board[ux][uy] = summary // cnt


result = 0
while True:
    visit = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n*n:
        break            
    result += 1
print(result)    
