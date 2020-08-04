from collections import deque
import sys
M, N = map(int, input().split())

matrix = [list(map(int,input().split())) for i in range(N)]
# print(matrix)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                queue.append([nx,ny])
                matrix[nx][ny] = matrix[x][y] +1

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i,j])
bfs()
result = -2 # -2보다 작을 수는 없으므로 최소값을 -2로 자븜
flag = False
for i in matrix:
    for j in i:
        if j == 0:  # 0이 하나라도 있으면 모두 익지 못하는 상황임
            flag = True
        result = max(result, j)
if flag == True: 
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)    
