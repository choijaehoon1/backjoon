N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for i in range(N)]
visit = [[0]*M for _ in range(N)]
# print(matrix)
# print(visit)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit[0][0] = 1
queue = [[0, 0]]

while queue:
    current_node = queue.pop(0)
    if current_node[0] == N -1 and current_node[1] == M -1:
        print(visit[N-1][M-1])
        break
    for k in range(4):
        nx = dx[k] + current_node[0]
        ny = dy[k] + current_node[1]
        if 0 <= nx < N and 0 <= ny <M:
            if visit[nx][ny] == 0 and matrix[nx][ny] == 1:
                visit[nx][ny] = visit[current_node[0]][current_node[1]] +1
                queue += [[nx,ny]]

