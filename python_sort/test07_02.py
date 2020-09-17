n = int(input())
arr = []

for i in range(n):
    data = input().split()
    arr.append((data[0],int(data[1]))) # 리스트안에 튜플형태로 값 저장

result =sorted(arr,key=lambda a: a[1])

for i in result:
    print(i[0],end=' ')

