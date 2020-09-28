test = int(input())

for i in range(test):
    result = ""
    data = list(map(str,input().split()))
    num = int(data[0])
    for k in data[1]:
        result += (k*num)
    print(result)        
