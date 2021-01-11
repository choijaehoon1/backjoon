# graph 배열 복사후 bfs 그래프를 다 0으로 만드는 것이 목표
from collections import deque
import copy
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 0이 접해있는 횟수 세는 함수
def check(x,y):
    num = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m and tmp_graph[nx][ny] == 0:
            num += 1
    return num

def bfs(x,y):
    q = deque()
    visit[x][y] = 1
    bfs_graph[x][y] = 0 
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny] == -1 and bfs_graph[nx][ny] !=0:
                    visit[nx][ny] = 1
                    bfs_graph[nx][ny] = 0
                    q.append([nx,ny])


result = 1
while True:
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    # 분리되지 않으면 종료                
    if cnt == n*m:
        print(0)
        break
    
    visit = [[-1]*m for _ in range(n)] 
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            # 기존 그래프의 값을 변경하는 것이 목적이므로 복사한 tmp_list 이용하여 처리
            # 기존 그래프로 처리시 0이 아닐때 조건에서 다르게 처리 됨
            if tmp_graph[i][j] != 0:
                tmp = check(i,j)
                if tmp_graph[i][j] - tmp < 0:
                    graph[i][j] = 0
                else:
                    graph[i][j] -= tmp

    bfs_graph = copy.deepcopy(graph) # graph 배열 복사후 bfs 그래프를 다 0으로 만드는 것이 목표
    group = 0
    for i in range(n):
        for j in range(m):
            if bfs_graph[i][j] != 0:
                bfs(i,j)
                group += 1 # bfs 그래프가 0이 아닐때만 (즉 영역이 나눠질때 하나씩 증가)
    if group >=2:
        print(result)
        break                
    result += 1                   

