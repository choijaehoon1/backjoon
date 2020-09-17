# 삽입정렬: 특정한 데이터를 적절한 위치에 삽입, 첫번째 데이터는
#           그 자체로 정렬되어 있다고 생각
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 첫번째 데이터부터 비교)
    for j in range(i,0,-1): # 0은 포함안되므로 1까지만임(즉 첫번째 데이터 신경x)
        if array[j] < array[j-1]: # 왼쪽으로 한칸씩 이동
            array[j], array[j-1] = array[j-1], array[j] # 스왑(즉 한칸씩 밀렸다 생각)
        else: # 더 작은 데이터를 만났으면 그때 멈춤
            break
print(array)        

