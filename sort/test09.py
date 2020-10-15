n = int(input())

array = []
for i in range(n):
    a,b = input().split()
    array.append((int(a),b,i))
# print(array)    

array.sort(key=lambda a: (a[0],a[2]))
# print(array)
for i in array:
    print(i[0],i[1])
