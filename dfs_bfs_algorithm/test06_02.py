r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(map(lambda x: ord(x)-65, input())))
# print(arr) # arr배열을 아스키코드로 바꾸 어줌

ch = [0] * 26 # 알파벳 개수
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,ans):
    global answer
    answer = max(answer, ans)
    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0<=nx<r and 0<=ny<c and ch[arr[nx][ny]] ==0:
            ch[arr[nx][ny]] = 1
            dfs(nx,ny,ans+1)
            ch[arr[nx][ny]] = 0

answer = 1
ch[arr[0][0]] = 1
dfs(0,0,answer)
print(answer)
