from collections import deque
n,m,v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visit = [0] * (n+1) # 정점 방문 확인

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)    

q = deque()

def bfs(v):
    visit[v] = 1
    q.append(v)
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(1,n+1):
            if graph[now][i] == 1 and visit[i] == 0:
                q.append(i)
                visit[i] = 1
bfs(v)
