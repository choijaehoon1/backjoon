n=int(input())

time = [0 for i in range(n+1)]
price = [0 for i in range(n+1)]
# dp[i]는 i날까지 일을 했을 때 최대값
dp = [0 for i in range(n+1)]
for i in range(n):
    a,b = map(int,input().split())
    time[i] = a
    price[i] = b

for i in range(len(time)-2,-1,-1): # 역순 진행
    if time[i] + i <= n: # 날짜 초과 안할 경우
        dp[i] = max(dp[time[i]+i]+price[i],dp[i+1])
    else: # 날짜 초과
        dp[i] = dp[i+1]    
print(dp[0])

