# dfs 예제 - 스택
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 연결된 정점 정보저장
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# visited = [False] *9
visited = [False for i in range(len(graph))]
# print(visited)
dfs(graph,1,visited) # 정점 1부터시작
