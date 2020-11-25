import sys
n = int(sys.stdin.readline().rstrip())

array = map(int, sys.stdin.readline().rstrip().split())

cnt = 0

for num in array:
    flag = True
    if num == 1:
        continue 

    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
    if flag == True:         
        cnt+=1

print(cnt)             

