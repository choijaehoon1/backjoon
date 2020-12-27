n = int(input())
dp = [n]
cnt = 0
while True:
    if 1 in dp:
        print(cnt)
        break
    s = []
    for i in dp:
        if i % 3 == 0:
            s.append(i/3)
        if i % 2 == 0:
            s.append(i/2)
        s.append(i-1)
    dp = s    
    cnt+=1                       
