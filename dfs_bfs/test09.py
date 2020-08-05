from collections import deque
N, M=map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
# print(matrix)

queue = deque()
queue.append([0,0,1])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    visit[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == N-1 and y == M -1:
            return visit[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if w == 1 and matrix[nx][ny] == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1  
                    queue.append([nx,ny,0])
                elif visit[nx][ny][w] == 0 and matrix[nx][ny] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1  
                    queue.append([nx,ny,w])
    return -1
print(bfs())                    
