# bfs로 풀이(시작점 부터 가까운 노드부터 탐색)
from collections import deque
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# print(graph)    
# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append([nx,ny])
                    visited[nx][ny] = True

visited = [[False]*m for _ in range(n)]
# print(visited)
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] ==False:
            bfs(i,j)
            cnt +=1
print(cnt)
