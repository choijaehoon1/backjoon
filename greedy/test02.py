from collections import deque
N = int(input())

queue = deque()

for i in range(N):
    start, end = map(int, input().split())
    queue.append([start,end])

# 끝나는 시간만 정렬된다면 (10, 10), (1, 1) 일때 결과가 1이 나옴
# 따라서 시작시간 끝나는 시간 둘다 정렬필요
queue = sorted(queue, key = lambda a: a[0])
queue = sorted(queue, key = lambda a: a[1])
# print(queue)

cnt = 0
tmp = 0
for start, end in queue:
    if start >= tmp:
        cnt += 1
        tmp = end
print(cnt)        
