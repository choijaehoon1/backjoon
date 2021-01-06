from collections import deque

R, C = map(int, input().split())

board = []
dist = [[-1]*C for _ in range(R)]
water = deque()

for i in range(R):
    board.append(list(input()))
    for j in range(C):
        if board[i][j] == 'S':
            s_x,s_y = i,j
        if board[i][j] == '*':
            water.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def water_bfs():
    # 완전 bfs가 아니라 매분마다 bfs 이므로 물의 개수에 따라 bfs수행
    water_cnt = len(water)
    while water_cnt: 
        x,y = water.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    water.append([nx,ny])
        water_cnt -= 1

def s_bfs(x,y):
    q = deque()
    q.append([x,y])
    dist[x][y] = 0 # 시작 최소 거리는 0
    board[x][y] = '.' # 이동할 수 있게 초기화

    while q:
        s_cnt = len(q)
        while s_cnt: # 고슴도치가 움직여서 있을 수 있는 위치만큼 bfs수행
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<R and 0<=ny<C:
                    if board[nx][ny] == '.' and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] +1
                        q.append([nx,ny])
                    if board[nx][ny] == 'D': # 다음에 비버굴이 있으면
                        print(dist[x][y]+1) # 현재 최단거리에서 +1한 것이 답
                        return    
            s_cnt -= 1            
        water_bfs() # 물 먼저 채우고 고슴도치 이동
    print("KAKTUS") # 도달하지 못한 경우 출력 후 리턴
    return

water_bfs() # 물을 먼저 채우고
s_bfs(s_x,s_y) # 고슴도치를 이동
