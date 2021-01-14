import sys
import heapq
n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    heapq.heappush(data,int(sys.stdin.readline().rstrip()))

result = 0
while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)

    sum_value = a+b
    result += sum_value
    heapq.heappush(data,sum_value)
print(result)
