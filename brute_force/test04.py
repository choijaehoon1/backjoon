n,m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(input()))

result = int(1e9) 
for i in range(n-7): # 8*8만 구하는 것이므로 check는 n-7, m-7번
    for j in range(m-7):
        num1, num2 = 0,0
        for x in range(i,i+8):
            for y in range(j,j+8):
                # 즉 BWBWBWBW
                if (x+y-i-j) % 2 == 0: # 짝수번째가 B
                    if array[x][y] == 'B':
                        num1 += 1
                else: #홀수번째까 W        
                    if array[x][y] == 'W':
                        num1 += 1

        for x in range(i,i+8):
            for y in range(j,j+8):
                # 즉 BWBWBWBW
                if (x+y-i-j) % 2 == 0: # 짝수번째가 W
                    if array[x][y] == 'W':
                        num2 += 1
                else: #홀수번째까 B
                    if array[x][y] == 'B':
                        num2 += 1                
        cnt = int(1e9)
        if num1 < num2:                
            cnt = num1
        else:
            cnt = num2    

        if result > cnt:
            result = cnt
print(result)            

