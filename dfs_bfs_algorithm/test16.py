# dp + dfs
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    if dp[x][y] != 0: # dp테이블을 방문한적이 있으면 바로 리턴
        return dp[x][y]
    dp[x][y] = 1
    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny)+1) # 새로운 dfs 수행하면 한칸 더 이동한 것
    return dp[x][y]

n = int(sys.stdin.readline().rstrip())
board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dp = [[0]*n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer,dfs(i,j))
print(answer)
