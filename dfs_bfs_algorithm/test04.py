from collections import deque
n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    de = deque()
    de.append([x,y])
    visit[x][y] = 1
    while de:
        current_node = de.popleft()
        for k in range(4):
            nx = dx[k] + current_node[0]
            ny = dy[k] + current_node[1]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                de.append([nx,ny])

answer = []
for i in range(101): # 물에 잠기는 높이에 따라 달라지므로 지정해줌
    visit = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] <=i:
                visit[j][k] = 1 # 침수

    for j in range(n):
        for k in range(n):
            if visit[j][k] == 0: # 침수 안된경우 방문 가능
                bfs(j,k)
                cnt+=1
    answer.append(cnt)
print(max(answer))


