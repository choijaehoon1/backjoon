n = int(input())
x = 1
y = 1
# 좌, 우, 상, 하 (L,R,U,D)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']
move = list(map(str,input().split()))

for i in move:
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx = dx[j] + x
            ny = dy[j] + y
    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue
    x = nx
    y = ny
print(x,y)            
