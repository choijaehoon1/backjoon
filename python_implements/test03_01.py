# 8방향
dx = [-1,1,-1,1,-2,-2,2,2]
dy = [-2,-2,2,2,-1,1,-1,1]

start = input() # str임
row = int(start[1])
column = int(ord(start[0])) - int(ord('a')) + 1 # 1열부터 시작이라는 가정

cnt = 0
for k in range(8):
    nx = row + dx[k]
    ny = column + dy[k]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    cnt += 1
print(cnt)

