from collections import deque

n,m = map(int, input().split())
target_list = list(map(int,input().split()))

q = deque()
for i in range(n):
    q.append(i+1)

cnt = 0
for i in range(m):
    length = len(q)
    index = q.index(target_list[i])

    if index < length - index: # 왼쪽이 가까움
        while True:
            if q[0] == target_list[i]:
                q.popleft()
                break
            else:
                q.append(q[0])
                q.popleft()
                cnt += 1     
    else:
        while True:
            if q[0] == target_list[i]:
                q.popleft()
                break
            else:
                q.appendleft(q[-1])
                q.pop()
                cnt+=1
print(cnt)                            
