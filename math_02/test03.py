import sys
import math
m,n = map(int,sys.stdin.readline().rstrip().split())

total = 0
min_num = int(1e9)
for num in range(m,n+1):
    if num == 1:
        flag = False
        continue
    flag = True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
            break    
    if flag == True:
        print(num)

