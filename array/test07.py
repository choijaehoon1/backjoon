N = int(input())

for i in range(N):
    arr = list(map(int,input().split(' ')))
    cnt = arr[0]
    sum = 0
    for i in range(1,len(arr)):
        sum += arr[i]
    avg = sum / cnt
    count = 0
    for i in range(1,len(arr)):
        if arr[i] > avg:
            count += 1

    print('%0.3f' % round(count/arr[0]*100,3) + '%')
