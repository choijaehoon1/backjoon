n = int(input())
arr = list(input())

answer = []
answer.append('*')

cnt = 0
for i in arr:
    if i == 'S':
        answer.append(i)
        answer.append('*')
    else: # i == 'L'
        if answer[-1] == 'L':
            answer.append(i)
            answer.append('*')
        else:
            answer.append(i)
ans = answer.count('*')
# 좌석이 하나인데 컵홀더가 두개면 ans는 1이다
if n < ans:
    print(n) # 사람의 수
else:
    print(ans)    


