n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0]
dp.append(arr[0])
if n > 1:
    dp.append(arr[0] + arr[1])
# dp에는 지금까지 먹은 것들 들어있음(2번째까지 먹었을때 경우의수)
# print(dp)

for i in range(3,n+1):
    case_01 = dp[i-1] # 이번에 안먹어야 함
    case_02 = arr[i-1] + dp[i-2] # 이번에 먹고 이전에 먹었음
    case_03 = arr[i-1] + arr[i-2] + dp[i-3] # 이번에 먹고 이전에꺼도 먹음(즉 맨처음에 안먹음)
    value = max(case_01,case_02,case_03)
    dp.append(value)
print(max(dp))    
