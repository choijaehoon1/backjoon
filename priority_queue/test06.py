import heapq
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

data.sort(key = lambda x:x[0])
h = []
for i in range(n):
    if len(h) != 0 and h[0] <= data[i][0]:
        heapq.heappop(h)
    heapq.heappush(h,data[i][1])
print(len(h))    
