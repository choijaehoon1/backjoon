N = int(input())

stack = []
answer = []
cnt = 1
check = True
for i in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        check = False 

if check:
    for i in answer:
        print(i)
else:
    print("NO")
