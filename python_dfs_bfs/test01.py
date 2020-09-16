# 스택 예제
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack) # 스택에 쌓여있는 순서(아래->위)
print(stack[::-1]) # 스택에 쌓여있는 순서(위->아래)

# 큐 예제
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue) # 먼저 들어온순서 대로 출력 [3,7,1,4]
print(list(queue)) # deque를 리스트형태로 변환가능
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력
