from collections import deque

n = int(input())
x,y = map(int,input().split())

m = int(input())

graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
visit = [0]*(n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    distance[x] = 0
    visit[x] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visit[i] == 0:
                visit[i] = 1
                distance[i] = distance[now] + 1
                q.append(i)            

bfs(x)

if distance[x] != -1 and distance[y] != -1:
    print(distance[x]+distance[y])
else:
    print(-1)    
