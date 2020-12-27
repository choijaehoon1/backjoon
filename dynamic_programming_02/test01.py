n,k = map(int, input().split())

price = []
for i in range(n):
    price.append(int(input()))

price.sort()
dp = [0]*(k+1)
dp[0] = 1 # 해당 동전 한개만 사용했을 때 값 추가하가 위해

for i in price:
    for j in range(i,k+1): # 해당 단위부터 k까지 dp[j-i]의 총개수 더해줌
        dp[j] += dp[j-i]
print(dp[k])        

