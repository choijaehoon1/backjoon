m = int(input())
n = int(input())

total = 0
min_num = int(1e9)
for num in range(m,n+1):
    if num == 1:
        flag = False
        continue
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break    
    if flag == True:
        total += num
        if min_num > num:
            min_num = num  
if min_num == int(1e9):
    print(-1)
else:
    print(total)
    print(min_num)                  

