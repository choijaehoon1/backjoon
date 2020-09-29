test = input().lower()
cnt = [0] * 26
arr_type =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(test)):
    if test[i] in arr_type:
        index = arr_type.index(test[i])
        cnt[index] += 1

max_index = 0
max_num = 0
tmp = 0
for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    
    if cnt[i] > max_num:
        max_index = i
        max_num = cnt[i]
        tmp = 0
    elif cnt[i] == max_num:
        tmp += 1

if tmp >= 1:
    print('?')
else:
    print(arr_type[max_index].upper())  
