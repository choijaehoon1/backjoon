import copy
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
ans = 0
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs():
    global ans
    copy_arr = copy.deepcopy(arr)
    
    for i in range(n):
        for j in range(m):
            if copy_arr[i][j] == 2:
                queue.append([i,j])
    while queue:
        current_node = queue.popleft()
        for k in range(4):
            nx = dx[k] + current_node[0]
            ny = dy[k] + current_node[1]
            if 0 <= nx < n and 0 <= ny < m and copy_arr[nx][ny] == 0:
                copy_arr[nx][ny] = 2 
                queue.append([nx,ny])

    cnt = 0
    for i in copy_arr: # 배열안 에서 0을 찾는 것임
        cnt += i.count(0) # bfs까지 했으니 0인곳은 안전한 곳임
    ans = max(ans,cnt) # 그때 그때마다 bfs한것 중 최대값    


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1 # 벽 세우기
                wall(cnt + 1)
                arr[i][j] = 0 # 원상 복구

queue = deque()
wall(0)
print(ans)
