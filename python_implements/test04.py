n,m = map(int, input().split()) # n은 세로크기(세로의 길이 = 행의 수), m은 가로크기(열의 수)
x,y,d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# 북, 동, 남, 서
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[0] * m for _ in range(n)]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1: # 북 -> 서
        d = 3
# 시뮬레이션 시작
visited[x][y] = 1
cnt = 1
turn_time = 0
while True:
    turn_left() # 왼쪽으로 회전
    nx = dx[d] + x
    ny = dy[d] + y 

    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else: # 바다이거나 이미 들렸던 곳
        turn_time += 1

    if turn_time == 4:
        # 방향은 유지한채 한칸 뒤로 이동
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break 
        turn_time = 0   
print(cnt)

