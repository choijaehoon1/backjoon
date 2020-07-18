N = int(input())

list = []
for i in range(0,N):
    str = input()
    str = str.split(' ')
    a = int(str[0])
    b = int(str[1])
    list.insert(i,a+b)
# print(enumerate(list))

cnt = 0
for i in list:
    cnt += 1
    print("Case #%d: %d" %(cnt,i))
