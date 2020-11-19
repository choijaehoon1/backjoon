n = int(input())

# 1부터 99까지는 한수이다
hansu = 0
for i in range(1,n+1):
    if i<100:
        hansu += 1
    else:
        tmp = list(map(int, str(i)))
        if tmp[0] - tmp[1] == tmp[1] - tmp[2]:
            hansu += 1
print(hansu)            
