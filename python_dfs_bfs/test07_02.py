from collections import deque
n,m =map(int,input().split())

graph = []
for _ in range(n): 
    graph.append(list(map(int,input())))
# print(graph)    

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # 튜플처럼 넣어도 가늠
    
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문하는 경우에만 최단 거리로 기록
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1 
    # 가장 오른쪽 아래 최단거리 값 반환
    return graph[n-1][m-1]            

print(bfs(0,0))

