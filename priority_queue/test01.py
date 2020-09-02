import heapq
import sys
n = int(sys.stdin.readline().rstrip())
heap = []
# heapq는 최소힙을 적용함( 우선순위큐 사용할 때 씀)
# 최대값을 구할려면 값에 -를 적용해서 최소힙으로 구현 후 -1을 다시 곱해 복구!
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num != 0: 
        heapq.heappush(heap, -num)
    else:
        if heap:
            print(heapq.heappop(heap) * -1)
        else:
            print(0)    
