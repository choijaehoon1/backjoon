n = int(input())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))    
array.sort(key= lambda a: (a[0],a[1]))
# print(array)
for i in array:
    print(*i)
