from collections import deque
import sys
def bfs(x,y):
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

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    l = int(sys.stdin.readline().rstrip())
    board = [[0]*l for _ in range(l)]
    visit = [[0]*l for _ in range(l)]

    start_x,start_y = map(int, sys.stdin.readline().rstrip().split())
    end_x,end_y = map(int, sys.stdin.readline().rstrip().split())
    result = int(1e9)
    bfs(start_x,start_y)
    print(board[end_x][end_y])
