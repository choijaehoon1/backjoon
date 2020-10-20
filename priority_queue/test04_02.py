import heapq
import sys
# 형제노드간에는 대소 상관 없음
left = [] # 중앙값보다 작은값
right = [] # 중앙값보다 큰 값

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if len(left) == len(right):
        # max heap(최대힙)
        heapq.heappush(left,(-num,num))
    else:
        # min heap(최소힙)
        heapq.heappush(right,(num,num))
    # 왼쪽값이 더 커진 경우
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(left,(-right_value,right_value))
        heapq.heappush(right,(left_value,left_value))
    # 중앙값을 max_heap의 맨 첫번째로 오게 구성    
    # print(left) [(-5, 5), (-2, 2), (99, -99), (-1, 1)]
    # print(right) [(5, 5), (10, 10), (7, 7)]
    print(left[0][1])    
