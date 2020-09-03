n = int(input())

arr = [0]+ list(map(int,input().split())) # 인덱스 맞춰 주기

dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i+1): # dp[i-j] + arr[j] 이런식으로 가면 결국 카드의 개수는 n이 됨
        dp[i] = max(dp[i], dp[i-j] + arr[j]) 
print(dp[-1])        
