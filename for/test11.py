a,b = map(int,input().split(' '))
list01 = list(map(int,input().split(' ')))

for i in range(a):
    if(b > list01[i]):
        print(list01[i], end=' ')
