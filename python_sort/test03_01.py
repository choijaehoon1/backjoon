# 퀵 정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end: # 원소가 하나인경우 종료
        return
    pivot = start # 첫번쨰 원소는 피봇
    left = start + 1 # 2번째 부터 시작
    right = end
    while left <= right:
        # 피봇보다 큰 데이터 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1 # 피봇이 더크면 오른쪽으로 한칸씩 증가
        # 피봇보다 작은 데이터 찾기(start는 피봇이므로 = 제거)
        while right > start and array[right] >= array[pivot]:
            right -=1 # 피봇보다 값이 더 크면 왼쪽으로 한칸씩
        # 엇갈린 경우
        if left > right: # 작은 데이터와 피봇과 교환
            array[pivot], array[right] = array[right], array[pivot]
        else: # 작은데이터와 큰데이터 교체
            array[left],array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬수행
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
