from collections import deque
M, N, H = map(int, input().split())
matrix = [[] for _ in range(H)]
visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        matrix[i].append(list(map(int,input().split())))

# print(matrix)
# print(visit)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
queue = deque()

def bfs():
    while queue:
        x,y,z = queue.popleft()
        visit[z][x][y] = 1
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if visit[nz][nx][ny] ==0 and matrix[nz][nx][ny] == 0:
                    queue.append([nx,ny,nz])
                    matrix[nz][nx][ny] = matrix[z][x][y] + 1 
                    visit[nz][nx][ny] = 1

for z in range(H):
    for x in range(N):
        for y in range(M):
            if matrix[z][x][y] == 1:
                queue.append([x,y,z])
bfs()

result = -2
flag = False
for z in range(H):
    for x in range(N):
        for y in range(M):
            if matrix[z][x][y] == 0:
                flag = True
            result = max(result, matrix[z][x][y])    

if flag == True:
    print(-1)
elif result == -1:     
    print(0)
else:
    print(result-1)

