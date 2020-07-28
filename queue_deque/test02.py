import sys
from collections import deque
N = int(sys.stdin.readline())

deque = deque()

for i in range(1,N+1):
    deque.append(i)

# print(len(deque))    
while len(deque) > 1:
    deque.popleft()
    a = deque.popleft()
    deque.append(a)

print(deque.pop())
