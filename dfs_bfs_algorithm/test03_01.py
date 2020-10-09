import sys
n,m = map(int, sys.stdin.readline().rstrip().split())

tmp = [[0]*m for _ in range(n)]
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer = 0

def virus(x,y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx,ny)

def get_score():
    result = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                result += 1
    return result

def dfs(count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i,j)
        answer = max(answer, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1                
dfs(0)
print(answer)
