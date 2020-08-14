# 각 자리에 올 수 있는 숫자의 개수를 세어 줌
# ex) 2자리 수 중 마지막 자리에 0이 올수 있는건 10 1개뿐
# 0부터 9까지 올 수 있는 숫자의 형태
# 한 자리수일 때 0  1  1  1  1  1  1  1  1  1
# 두 자리수일 때 1  1  2  2  2  2  2  2  2  1

n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
# print(dp)
for i in range(1,10):
    dp[1][i] = 1
# print(dp)    
for i in range(2,n+1): # 한자리 수 일때는 해당 반복문 영향 x
    for j in range(10):
        if j == 0:  # 오른쪽 위 대각선의 값만 받음
            dp[i][j] = dp[i-1][1]
        elif j == 9: # 왼쪽 위 대각선의 값만 받음
            dp[i][j] = dp[i-1][8]
        else: # 양 대각선의 값 더해서 받음
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# print(dp)
print(sum(dp[n]) % 1000000000)                    

