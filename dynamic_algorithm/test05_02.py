n = int(input())

arr = [0]+ list(map(int,input().split())) # 인덱스 맞춰 주기

dp = [0 for _ in range(n+1)]
dp[1] = arr[1] # 한개를 사는 경우는 당연히 처음 값임

for i in range(2,n+1):
    for j in range(1,i+1):
        if dp[i] < dp[i-j] + arr[j]: # n개 맞춰주기
            dp[i] = dp[i-j] + arr[j]
print(dp[n])            

# dp[2] = dp[0]+ arr[2] or dp[1] + arr[1]
# dp[3] = dp[0] + arr[3] or dp[1] + arr[2] or dp[2] + arr[1]
# dp[4] = dp[0] + arr[4] or dp[1] + arr[3] or dp[2] + arr[2] or dp[3] + arr[1]
# 즉 dp[n]일떄인덱스 둘이 더한것이 n 이 되야함
