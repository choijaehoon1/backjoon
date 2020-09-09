r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(input()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global answer
    queue = set([(x,y,arr[x][y])]) # 튜플로 만들고 리스트로 감싼 후에 set함수를 적용 
    while queue: # queue는 set임                
        current_node = queue.pop()
        alpha = current_node[2]
        for k in range(4):
            nx = dx[k] + current_node[0]
            ny = dy[k] + current_node[1]
            if 0<=nx<r and 0<=ny<c and arr[nx][ny] not in alpha:
                queue.add((nx,ny,alpha + arr[nx][ny])) # set은 add함수 사용
                answer = max(answer,len(alpha)+1) # 해당 조건문에 들어왔으면 alpha길이 +1을 해준것이 최대임
                                                  # 아직 alpha의 길이에 새로운 알파벳이 추가되기 이전이므로
answer = 1
bfs(0,0)
print(answer)
