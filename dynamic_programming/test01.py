N = int(input())

arr = []
for i in range(N+1):
    if i == 0 or i == 1:
        arr.append(i)
    else:
        tmp = arr[i-2] + arr[i-1]
        arr.append(tmp)        
print(arr[N])        
