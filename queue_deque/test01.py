import sys
from collections import deque
class Queue():
    def __init__(self):
        self.deque = deque()

    def push(self, num):
        self.deque.append(num)

    def pop(self):
        if deque.size() == 0:
            return -1
        else:    
            return self.deque.popleft()

    def size(self):
        return len(self.deque)

    def empty(self):
        if deque.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if deque.size() == 0:
            return -1
        else:
            return self.deque[0]    

    def back(self):
        if deque.size() == 0:
            return -1
        else:
            return self.deque[-1]      

deque = Queue()
N = int(sys.stdin.readline())

for i in range(N):
    str = sys.stdin.readline().rstrip().split(' ')
    if str[0] == 'push':
        deque.push(int(str[1]))
    elif str[0] == 'front':
        print(deque.front())
    elif str[0] == 'size':
        print(deque.size())
    elif str[0] == 'empty':
        print(deque.empty())
    elif str[0] == 'back':
        print(deque.back())
    elif str[0] == 'pop':
        print(deque.pop())
