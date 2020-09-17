n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(str,input().split())))

result =sorted(arr,key=lambda a: int(a[1]))

for i in range(len(result)):
    print(result[i][0],end=' ')

