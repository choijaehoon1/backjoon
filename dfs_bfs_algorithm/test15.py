import heapq
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append((b,c))

start,depart = map(int,sys.stdin.readline().rstrip().split())

dist = [INF for _ in range(n+1)]
h = []
heapq.heappush(h,(0,start))
dist[start] = 0

while h:
    cost,now = heapq.heappop(h)
    if cost < dist[now]:
        continue
    for i in graph[now]:
        if cost + i[1] < dist[i[0]]:
            dist[i[0]] = cost + i[1]
            heapq.heappush(h,(cost + i[1],i[0]))
print(dist[depart])


