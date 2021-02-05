import sys
n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp = [0 for _ in range(n)]
if n == 1:
    print(data[0][2]) 
else:
    dp[0] = data[0][2]
    dp[1] = data[1][2]
    answer = max(dp[0],dp[1])
    for i in range(2,n):
        for j in range(i-2,-1,-1):
            dp[i] = max(dp[i],dp[j] + data[i][2])        
    print(max(dp))
