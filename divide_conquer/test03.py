n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
# print(arr)    

zero_cnt = 0
one_cnt = 0
minus_one_cnt = 0

def check(x,y,n):
    global zero_cnt, one_cnt, minus_one_cnt
    tmp = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tmp != arr[i][j]: # 다르면 9등분하기
                for a in range(3): 
                    for b in range(3):
                        check(x+n//3*a,y+n//3*b,n//3)
                return        
    if tmp == 1:
        one_cnt += 1
    elif tmp == 0:
        zero_cnt +=1
    elif tmp == -1:
        minus_one_cnt +=1        

check(0,0,n)
print(minus_one_cnt)
print(zero_cnt)
print(one_cnt)
