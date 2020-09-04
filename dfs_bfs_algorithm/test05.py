from collections import deque
m,n,k = map(int, input().split())
arr = [[0]*n for _ in range(m)]

square = []
for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            arr[j][k] = -1 # 갈 수 없는곳

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()

def bfs(x,y,cnt):
    queue.append([x,y])
    arr[x][y] = cnt
    while queue:
        current_node = queue.popleft()
        for k in range(4):
            nx = dx[k] + current_node[0]
            ny = dy[k] + current_node[1]
            if 0<= nx < m and 0<= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = cnt
                queue.append([nx,ny])

cnt = 1 # 0 부터 잡으면 0으로 표시되어있는 것과 겹치므로 1부터 시작
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            bfs(i,j,cnt)
            cnt += 1
cnt -= 1 # 다시 1 감소 시켜줌
print(cnt)
# print(arr)
answer = [0] * cnt # 배열을 만들어줌
for i in range(m):
    for j in range(n):
        if arr[i][j] > 0:
            answer[arr[i][j]-1] += 1 # arr[i][j]-1는 답의 0,1,2 위치가 나오게 만들어 줌
answer.sort()
print(*answer)            
