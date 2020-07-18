num = int(input())
num_list = list(map(int,input().split(' ')))

max = num_list[0]
min = num_list[0]

for i in num_list:
    if(max < i):
        max = i
    if(min > i):
        min = i
print(min, max)
