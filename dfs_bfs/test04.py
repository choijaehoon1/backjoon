test_case = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = [[x,y]]
    while queue:
        current_node = queue.pop(0)
        for k in range(4):
            nx = dx[k] + current_node[0]
            ny = dy[k] + current_node[1]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] ==1:
                queue += [[nx,ny]]
                visit[nx][ny] = 0


for _ in range(test_case):
    M,N,K = map(int,input().split())
    visit = [[0]*M for _ in range(N)]
    cnt = 0    
    for _ in range(K):
        x, y = map(int,input().split()) # 좌표는 열, 행순으로 받음
        visit[y][x] =1
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 1:
                bfs(i,j)
                visit[i][j] = 0
                cnt += 1    
    print(cnt)    
