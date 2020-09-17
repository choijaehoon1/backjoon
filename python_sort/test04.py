# 계수정렬: 특정한 조건이 부합할 때만 사용가능
#           비교기반 알고리즘이 아니다

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] 
# (새로운 리스트: 가장큰데이터 - 가장작은데이터)
count = [0] * (max(array)+1) # 가장 큰 값에서 +1을 해주면됨(0부터 이므로)

# 각 데이터에 해당하는 인덱스 값 더하기
for i in range(len(array)):
    count[array[i]] += 1
    
# 리스트에 기록된 정보 확인
for i in range(len(count)): 
    for j in range(count[i]):
        print(i,end='')

