n = int(input())

cnt = 0
for i in range(n):
    arr = []
    data = input()
    flag = True
    for k in range(len(data)-1):
        if data[k] == data[k+1]:
            continue
        if data[k+1] in arr or data[k] in arr:
            flag = False
            break
        arr.append(data[k])
    if flag == True:        
        cnt += 1
print(cnt)        
