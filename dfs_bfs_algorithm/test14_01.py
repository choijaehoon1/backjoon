# bfs리스트에 group 값 적용하여 풀기
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

def bfs(x,y,group):
    q = deque()
    visit[x][y] = 1
    group_list[x][y] = group
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny] == -1 and graph[nx][ny] != 0:
                    visit[nx][ny] = 1
                    group_list[nx][ny] = group
                    q.append([nx,ny])


total_cnt = 1
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
    
    tmp_graph = copy.deepcopy(graph) # tmp배엷 복사
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
    
    group = 0
    visit = [[-1]*m for _ in range(n)] 
    group_list = [[-1]*m for _ in range(n)] # 그룹 리스트
    for i in range(n):
        for j in range(m):
            # 그래프의 값이 0이 아니고 방문하지 않았을때만 같은 그룹
            if graph[i][j] != 0 and visit[i][j] == -1:
                group += 1
                bfs(i,j,group)
    # 2개 이상이면 종료                                
    if group >=2:
        print(result)
        break                
    total_cnt += 1 # 전체 횟수 증가              
