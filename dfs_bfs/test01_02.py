from collections import deque
n,m,v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visit = [0] * (n+1) # 정점 방문 확인

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)    

def dfs(v):
    visit[v] = 1 # 방문처리
    print(v, end=' ')
    for i in range(1,n+1):
        # v와 연겱된 정점
        if graph[v][i] == 1 and visit[i] == 0:
            dfs(i)
dfs(v)
