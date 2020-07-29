from collections import deque

queue = deque()

cnt = int(input())

for i in range(cnt):
    N,M = map(int,input().split())
    queue = deque(input().split())
    queue2 = deque(range(len(queue)))
    queue2[M] = 'target'

    order = 0
    while True:
        if queue[0] == max(queue):
            order += 1
            if queue2[0] == 'target':
                print(order)
                break
            else:
                queue.popleft()
                queue2.popleft()
        else:
            queue.append(queue.popleft()) 
            queue2.append(queue2.popleft())
