N = int(input())

for i in range(N):
    stack = list(input())
    while len(stack) != 0:
        if stack[0] == ')' or stack[-1] =='(':
            print("NO")
            break
        else:
            if '(' and ')' in stack:
                stack.pop(stack.index(')') -1)
                stack.pop(stack.index(')'))
    if len(stack) == 0:
        print("YES")
