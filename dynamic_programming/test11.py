n = int(input())
arr = list(map(int, input().split()))
# print(arr)
dp = [0 for i in range(n)]
# print(dp)
for i in range(n):
    for j in range(i):
        # 자기자신보다 작은 숫자들 중에 가장 큰 길이를 구함
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    # 그 길이에 +1 을 해준다.        
    dp[i] += 1
# print(dp)
print(max(dp))
