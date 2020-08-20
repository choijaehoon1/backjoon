n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
# print(arr)    

blue = 0
white = 0

def check(x,y,n):
    global blue, white
    tmp_color = arr[x][y]
    flag = True

    for i in range(x,x+n):
        if flag == False: # 매개변수로 받은 색상이 다르면
            break         # 더이상 조사할 필요 x
        for j in range(y,y+n):
            if tmp_color != arr[i][j]:
                flag = False
                check(x,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y,n//2)
                check(x+n//2,y+n//2,n//2)
                break
    if flag ==True:
        if tmp_color == 1:                    
            blue += 1
        else:
            white += 1    
check(0,0,n)
print(white)
print(blue)
