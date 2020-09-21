n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [10001] * (m+1)
# 0원인 경우 화폐를 사용하지 않고도 만들 수 있음
dp[0] = 0

# k는 화폐의 딘위
# 점화식은 min(dp[i],dp[i-k]+1) 
for i in range(n): # 화폐의 개수(단위)만큼 확인
    for j in range(arr[i],m+1): # j는 화폐단위부터 m까지 반복
        if dp[j-arr[i]] != 10001: # if문은 생략가능
            dp[j] = min(dp[j],dp[j-arr[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])                
