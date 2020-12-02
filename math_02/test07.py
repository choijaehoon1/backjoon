array_x = []
array_y = []
for _ in range(3):
    x,y = map(int, input().split())
    array_x.append(x)
    array_y.append(y)

answer = [0,0]
for i in range(len(array_x)):
    cnt_x = array_x.count(array_x[i])
    cnt_y = array_y.count(array_y[i])
    if cnt_x == 1:
        answer[0] = array_x[i]
    if cnt_y == 1:
        answer[1] = array_y[i]
print(*answer)        
