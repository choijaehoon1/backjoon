from collections import deque

def bfs(x,y,array,visit):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1

    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<l and 0<=ny<l and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1
                q.append([nx,ny])
                
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

tc = int(input())
for _ in range(tc):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    visit = [[0]*l for _ in range(l)]

    start_x,start_y = map(int, input().split())
    end_x,end_y = map(int, input().split())
    result = int(1e9)
    bfs(start_x,start_y,board,visit)
    print(board[end_x][end_y])

