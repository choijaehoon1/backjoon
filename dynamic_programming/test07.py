n = int(input())
arr = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    num = int(input())
    arr[i] = num
# print(arr)    

dp[0] = arr[0] # 첫번째계단올라가는방법          
dp[1] = arr[0] + arr[1] # 두번째계단올라가는방법
dp[2] = max(arr[0] + arr[2], arr[1]+ arr[2]) # 세번째계단올라가는방법

for i in range(3,n):
    # 마지막전 계단 밞고 마지막에 도착하는 경우와 마지막전전계단밞고 마지막 도착하는 경우
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], + dp[i-2] + arr[i])
print(dp[n-1])    
