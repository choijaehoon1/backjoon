from collections import deque
a, b = map(int, input().split(' '))

queue = deque()
arr = []

for i in range(1,a+1):
    queue.append(i)

while len(queue) > 1:
    for i in range(b-1):
        num = queue.popleft()
        queue.append(num)
    arr.append(queue.popleft())
arr.append(queue.popleft())            

print("<"+ ", ".join(map(str,arr)) + ">")
