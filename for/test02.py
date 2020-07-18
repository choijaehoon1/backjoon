N = int(input())
list = []
for i in range(0,N):
    str = input()
    str = str.split(' ')
    a = int(str[0])
    b = int(str[1])
    list.append(a+b)
# print(list)
for i in list:
    print(i)
