n= int(input())

array = []
for _ in range(n):    
    array.append(input())
set_array = list(set(array))
# print(set_array)

result = []
for i in set_array:
    result.append((len(i),i))
result.sort()
for i in result:
    print(i[1])
