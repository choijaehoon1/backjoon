# dfs로 풀이
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 주어진 범위 벗어나는 경우 check
    if x <=-1 or x >= n or y <= -1 or y >= m:
        return False
    # 상하좌우 그룹으로 묶어준다 생각(True일때만 원하는 그룹임)
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 해당 위치에서 dfs 수행
        if dfs(i,j) == True:
            result +=1
print(result)

