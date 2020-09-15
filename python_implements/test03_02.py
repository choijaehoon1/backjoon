# 8방향
steps = [(-1,-2),(1,-2),(-1,2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]

start = input() # str임
row = int(start[1])
column = int(ord(start[0])) - int(ord('a')) + 1 # 1열부터 시작이라는 가정

cnt = 0
for i in steps:
    new_row = i[0] + row
    new_column = i[1] + column
    if (new_row >= 1 and new_row <=8) and (new_column >=1 and new_column <=8):
        cnt+=1
print(cnt)

