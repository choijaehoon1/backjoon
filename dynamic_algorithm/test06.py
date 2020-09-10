test = int(input())

for _ in range(test):
    n = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int,input().split())))
    arr[0][1] += arr[1][0] # 처음에는 대각선에 있는 값 더해야 함
    arr[1][1] += arr[0][0] # 처음에는 대각선에 있는 값 더해야 함

    for i in range(2,n): # 2번째부터는 왼쪽대각선숫자와 그 왼쪽숫자 중 큰 값 더해줌
        arr[0][i] += max(arr[1][i-1],arr[1][i-2])        
        arr[1][i] += max(arr[0][i-1],arr[0][i-2])
    print(max(arr[0][n-1],arr[1][n-1]))

