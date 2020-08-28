n = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(n)]

for i in range(1,n+1): # 1,2,3... 키를 나타내는 것
    tmp = arr[i-1]
    cnt = 0
    for j in range(n):
        if cnt == tmp and ans[j] == 0:
            ans[j] = i # 그 떄의 위치에 키를 삽입 
            break # ex) 키 1 짜리는 왼쪽에 2개 있고 3번째 위치에 위치한다.
        elif ans[j] == 0:
            cnt += 1
print(*ans)            
