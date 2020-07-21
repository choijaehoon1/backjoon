import sys

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack == []:  
            return 1
        else:
            return 0
    def top(self):
        if self.stack == []:
            return -1
        else:
            return self.stack[-1]

stack = Stack()

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    str = sys.stdin.readline().rstrip().split(' ')
    if str[0] == 'push':
        stack.push(str[1])
    elif str[0] == 'pop':
        print(stack.pop())
    elif str[0] == 'size':
        print(stack.size())
    elif str[0] == 'empty':
        print(stack.empty())
    elif str[0] == 'top':
        print(stack.top())
