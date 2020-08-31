import sys
sys.setrecursionlimit(10000)

n,m = map(int, sys.stdin.readline().split())
visit = [0 for i in range(n+1)]
arr = [[0] * (n+1) for i in range(n+1)] # 0행 0열은 간선이 없으므로 안씀

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1    

def dfs(v):
    visit[v] = 1
    for i in range(1,n+1):
        if arr[v][i] == 1 and visit[i] == 0:
            dfs(i)
cnt = 0
for i in range(1,n+1):
    if visit[i] == 0:
        dfs(i)
        cnt+=1        
print(cnt)
