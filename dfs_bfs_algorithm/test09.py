from collections import deque
n,m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input()))

visit = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(x,y,dx,dy):
    cnt = 0
    # 다음칸이 막혀있지 않고 현재 구멍이 아닌 경우를 구하기
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt    

def bfs(rx,ry,bx,by,depth):
    q = deque()
    q.append([rx,ry,bx,by,depth])
    visit[rx][ry][bx][by] = 1
    while q:
        rx,ry,bx,by,depth = q.popleft()
        if depth > 10:
            return -1 
        for k in range(4):
            nrx,nry,r_cnt = move(rx,ry,dx[k],dy[k])
            nbx,nby,b_cnt = move(bx,by,dx[k],dy[k])
            if board[nbx][nby] != 'O': # 파란색이 구멍에 안들어간 경우
                if board[nrx][nry] == 'O': # 빨간색이 구멍에 들어간 경우
                    return depth
            
                if nrx == nbx and nry == nby: # 같은 위치일 경우 조정(전제는 파란색이 구멍이 아닌 경우)
                    if r_cnt > b_cnt:
                        nrx -= dx[k]
                        nry -= dy[k]
                    else:
                        nbx -= dx[k]
                        nby -= dy[k]

                if visit[nrx][nry][nbx][nby] == 0:
                    visit[nrx][nry][nbx][nby] = 1
                    q.append([nrx,nry,nbx,nby,depth+1])
    return -1


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri,rj = i,j
        if board[i][j] == 'B':
            bi,bj = i,j

result = bfs(ri,rj,bi,bj,1)
print(result)

 
