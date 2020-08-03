N = int(input())

visit = [[0]*N for _ in range(N)]
a = [list(map(int,list(input()))) for _ in range(N)]
# print(a)
# print(visit)

cnt = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y, cnt):
    queue = [[x,y]] # 이중배열
    visit[x][y] = cnt
    while queue:
        current_node = queue.pop(0) # 0번째 인덱스인 리스트 하나가 나옴
        for k in range(4):
            nx = current_node[0] + dx[k]
            ny = current_node[1] + dy[k] 
            if (nx >= 0 and  nx < N) and (ny >= 0 and  ny < N):
                if visit[nx][ny] == 0 and a[nx][ny] == 1: # 방문하지 않았고 연결되어있으면    
                    visit[nx][ny] = cnt
                    queue += [[nx,ny]]    

for i in range(N):
    for j in range(N):
        if a[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

# 1 차원 리스트로 만들기
answer = []
for i in visit:
    answer += i 
# 총단지수    
print(max(answer))    

arr = []
for i in range(1,max(answer)+1):
    sum = 0
    for j in answer:
        if i == j:
            sum += 1
    arr.append(sum)

arr.sort()

for i in arr:
    print(i)

