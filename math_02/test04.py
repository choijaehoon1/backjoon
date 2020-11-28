import sys
import math

while True:
    n = int(sys.stdin.readline().rstrip())
    cnt = 0
    if n == 0:
        break
    for num in range(n+1,2*n+1):
        flag = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                flag = False
                break    
        if flag == True:
            cnt += 1
    print(cnt)                

