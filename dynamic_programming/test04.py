test = int(input())
for _ in range(test):
    arr = []
    n = int(input())
    for i in range(n):
        if i == 0 or i ==1 or i ==2:
            arr.append(1)
        else:
            tmp = arr[i-3] + arr[i-2]    
            arr.append(tmp)
    print(arr[-1])
