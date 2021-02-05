import sys
n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp = [0 for _ in range(n)]
if n == 1:
    print(data[0][2])
elif n == 2:
    dp[0] = data[0][2]
    dp[1] = data[1][2]
    print(max(dp[0],dp[1]))
else:
    dp[0] = data[0][2]
    dp[1] = data[1][2]
    dp[2] = max(dp[0] + data[2][2], dp[1])

    for i in range(3,n):
        dp[i] = max(dp[i-2],dp[i-3]) + data[i][2]
    print(max(dp))
