import math
n = int(input())

if n == 0: # 0!은 1이다.
    print(0)
else:
    str_n= str(math.factorial(n))
    result = 0
    for i in range(len(str_n)-1,-1,-1):
        if str_n[i] != '0':
            break
        result += 1
    print(result)    
