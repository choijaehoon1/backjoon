# 선택정렬: 가장 작은 데이터를 맨앞에 데이터와 바꾸고
#           그다음 작은 데이터를 두번째 데이터와 바꾸는 형태
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 스와핑(python에서는 간단히 가능)            
    array[i], array[min_index] = array[min_index], array[i]
print(array)      
