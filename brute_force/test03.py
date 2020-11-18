n = int(input())
array = []
for _ in range(n):
    a,b = map(int,input().split())
    array.append((a,b))
# print(array)    

for i in range(n):
    k = 1
    for j in range(n):
        if i == j:
            continue
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            k += 1
                     
    print(k,end=' ')
