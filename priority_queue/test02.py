import heapq
import sys
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0: # num이 0일때는 출력하는 것이고 아닐때는 push
        heapq.heappush(heap,num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
