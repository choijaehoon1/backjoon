from collections import deque
import sys
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(x,y,array,visit,l):
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
                array[nx][ny] = array[x][y] + 1
                q.append([nx,ny])
                
def solution():
    l = int(sys.stdin.readline().rstrip())
    board = [[0]*l for _ in range(l)]
    visit = [[0]*l for _ in range(l)]

    start_x,start_y = map(int, sys.stdin.readline().rstrip().split())
    end_x,end_y = map(int, sys.stdin.readline().rstrip().split())
    result = int(1e9)
    bfs(start_x,start_y,board,visit,l)
    return board[end_x][end_y]

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    print(solution())
