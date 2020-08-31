dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,-1,-1,1,1]

def bfs(x,y,cnt):
    queue = [[x,y]]
    arr[x][y] = 0
    while queue:
        current_node = queue.pop(0)
        for k in range(8):
            nx = dx[k] + current_node[0]
            ny = dy[k] + current_node[1]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] ==1:
                arr[nx][ny] = 0
                queue += [[nx,ny]]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    arr =[]
    for i in range(h):
        arr.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] ==1:
                cnt += 1
                bfs(i,j,cnt)
    print(cnt)
