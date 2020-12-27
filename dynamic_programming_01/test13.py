n = int(input())
w = [list(map(int, input().split())) for i in range(n)]
# a전봇대 기준으로 정렬
w.sort(key= lambda x:x[0])
# print(w)    

w_b = []
dp = [0 for i in range(n)]

# b전봇대
for i in range(n):
    w_b.append(w[i][1])
# print(w_b)

# b전봇대에서 가장 긴 증가하는 부분수열 구해주기
for i in range(n):
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
# print(dp)
# 없앨 최소 전기줄은 입력받은 값에서 가장 큰 부분수열의 값뺴주기
print(n - max(dp))            
