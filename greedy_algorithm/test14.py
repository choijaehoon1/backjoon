n=int(input())

meter = list(map(int,input().split()))
city_price = list(map(int,input().split()))

meter.append(0) # 인덱스 맞춰주기 용
answer = 0

dp = [0 for i in range(n+1)]

dp[0] = city_price[0] * meter[0] # 처음에는 선택지가 없음(무조건 다음까지 가야함)
min = city_price[0]

for i in range(1,n):
    if min > city_price[i]:
        min = city_price[i]
    dp[i] = dp[i-1] + (min * meter[i])
print(dp[n-1])        
