import math
import sys
from itertools import combinations_with_replacement

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    n = int(sys.stdin.readline().rstrip())
    array = []
    for num in range(2,n+1):
        flag = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                flag = False
                break
        if flag == True:
            array.append(num)

    tmp_list = list(combinations_with_replacement(array,2)) # 조합도 허용

    result_list = []
    for x,y in tmp_list:
        num = x + y
        if num == n:
            result_list.append((x,y))
    min_result = int(1e9)
    answer = [int(1e9),int(1e9)]            
    if len(result_list) == 1:
        print(result_list[0][0],result_list[0][1])
    elif len(result_list) >= 2:        
        for i in range(len(result_list)):
            if (n//2) > result_list[i][0]:
                continue
            else:
                print(result_list[i][0],result_list[i][1])
                break
