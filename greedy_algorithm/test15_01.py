n = int(input())
arr = list(input())

answer = []
answer.append('*')

cnt = 0
for i in arr:
    if i == 'S':
        answer.append('*')
    else: # i == 'L'
        cnt += 1     
    if cnt == 2:
        answer.append('*')
        cnt = 0
ans = answer.count('*')
# 좌석이 하나인데 컵홀더가 두개면 ans는 1이다
if n < ans:
    print(n) # 사람의 수
else:
    print(ans)    

