# 특정 위치에서 최단걸를 구하는 함수
def bfs(x,y):
    dist = [[-1]*n for _ in range(n)]
    q = deque()
    q.append([x,y])
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<n and 0<=ny<n:
                # 방문하지 않았고 사이즈가 같거나 작을때는 이동가능
                if dist[nx][ny] == -1 and board[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    return dist


def find(tmp_x,tmp_y):
    global time
    global ate
    global size
    global start_x
    global start_y
    
    tmp_dist = bfs(tmp_x,tmp_y)
    # 최단 거리 비용 찾기
    min_value = int(1e9)
    for i in range(n):
        for j in range(n):
            if tmp_dist[i][j] < min_value and tmp_dist[i][j] != -1 and board[i][j] < size and board[i][j] != 0:
                min_value = tmp_dist[i][j]

    if min_value == int(1e9):
        return False
    # 최단 거리인 좌표들 찾아서 저장    
    next_pos = []
    for i in range(n):
        for j in range(n):
            if tmp_dist[i][j] == min_value and board[i][j] != 0 and board[i][j] < size:
                next_pos.append([i,j])
    
    if next_pos:
        next_pos.sort(key=lambda x: (x[0],x[1]))
        start_x,start_y = next_pos[0] # 시작위치 갱신(전역변수)
        ate += 1 
        time += min_value
        board[start_x][start_y] = 0 # 시작위치의 좌표는 0으로 갱신
        return True
    else:
        return False    



from collections import deque
n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 9:
            # 시작 위치 저장 후 0으로 변환
            start_x,start_y = i,j
            board[i][j] = 0
        
dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = 0
size = 2
ate = 0
while True:
    if not find(start_x,start_y):
        break
    # 먹은 횟수 초기화 및 크기 증가
    if ate >= size:
        ate = 0
        size += 1
print(time)
