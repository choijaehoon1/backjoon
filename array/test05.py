N= int(input())
str_list = list(map(int,input().split(' ')))

result_list = []
for i in str_list:
    max_num = max(str_list)
    a = i/max_num*100
    result_list.append(a)

avg = 0
sum = 0
for i in result_list:
    sum += i
    avg = sum / len(result_list)
print(avg)
