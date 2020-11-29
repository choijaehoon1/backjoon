import math
import sys

def search_sosu(n):
    flag = [True] * n
    for i in range(2,int(math.sqrt(n))+1):
        if flag[i] == True:
            for j in range(2*i,n,i): # 그 다음 i만큼은 다 소수가 안됨
                flag[j] = False
    return [i for i in range(2,n) if flag[i] == True]            

tc = int(input())
for _ in range(tc):
    n = int(input())   
    result_list = search_sosu(n)    
    # 절반값 보다 작은 수중 가장 큰 인덱스 구하는 것
    idx = max([i for i in range(len(result_list)) if result_list[i] <= n//2])
    a = 0
    b = 0
    # 작은 소수 찾는 과정
    for i in range(idx,-1,-1):
        for j in range(i,len(result_list)):
            if result_list[i] + result_list[j] == n:
                a = result_list[i]
                b = result_list[j]
                break
        if a != 0 and b != 0:
            break    
    
    print(a,b)                
