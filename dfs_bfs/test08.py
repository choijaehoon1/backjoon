from collections import deque

N, M = map(int, input().split()) 
visit = [0 for _ in range(100001)]

queue = deque()
queue.append([N,0])
# print(queue)
while queue:
    pos = queue[0][0]
    depth = queue[0][1]

    if pos == M: # 기준점이 됫을때의 depth를 찍으면 최단거리임
        break
    queue.popleft()
    visit[pos] = 1
    if pos-1 >= 0 and visit[pos-1] == 0:
        queue.append([pos-1, depth+1])
    if pos+1 <= 100000 and visit[pos+1] == 0:
        queue.append([pos+1, depth+1])
    if pos*2 <= 100000 and visit[pos*2] == 0:
        queue.append([pos*2, depth+1])        

print(queue[0][1])
