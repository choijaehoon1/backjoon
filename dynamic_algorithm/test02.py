# 1, 2, 3, 5, 8
n = int(input())
dp = [0 for i in range(n+1)]

for i in range(1,n+1):
    if i == 1 or i==2:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)    
