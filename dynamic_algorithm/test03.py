n = int(input())

dp = [0 for i in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        dp[i] = i
    elif i == 2:
        dp[i] = dp[i-1]*2 +1        
    else:    
        dp[i] = dp[i-2]*2 + dp[i-1]
print(dp[n]%10007)
