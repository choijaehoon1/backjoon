from collections import deque
import sys
class Deque():
    def __init__(self):
        self.queue = deque()

    def push_front(self, value):
        self.queue.appendleft(value)

    def push_back(self, value):   
        self.queue.append(value)

    def pop_front(self):
        if queue.size() == 0:
            return -1
        else:
            return self.queue.popleft()

    def pop_back(self):
        if queue.size() == 0:
            return -1
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        if queue.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if queue.size() == 0:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if queue.size() == 0:
            return -1
        else:
            return self.queue[-1]        

queue = Deque()

N = int(sys.stdin.readline())
for i in range(N):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == 'push_back':
        queue.push_back(str[1])
    elif str[0] == 'push_front': 
        queue.push_front(str[1])
    elif str[0] == 'front':
        print(queue.front())
    elif str[0] == 'back':
        print(queue.back())
    elif str[0] == 'pop_front':
        print(queue.pop_front())
    elif str[0] == 'pop_back':
        print(queue.pop_back())
    elif str[0] == 'size':
        print(queue.size())
    elif str[0] == 'empty':
        print(queue.empty())
