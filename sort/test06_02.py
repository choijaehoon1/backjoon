import sys
n = int(sys.stdin.readline().rstrip())

array = []
for i in range(n):
    array.append(list(map(int,sys.stdin.readline().rstrip().split())))    
array.sort(key= lambda a: (a[0],a[1]))
# print(array)
for i in array:
    print(i[0],i[1])
