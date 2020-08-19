N, K = map(int, input().split())
s = []
for i in range(N):
    s.append(list(map(int, input().split())))
# print(s) 
w = []
v = []
for i in range(N):
    w.append(s[i][0])
    v.append(s[i][1])   

dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = w[i-1] # 해당 물건의 무게
        value = v[i-1]  # 해당 물건의 가치

        if j < weight: # 무게가 더 크면 이전값이 옴
            dp[i][j] = dp[i-1][j]
        else: # j가 해당 무게보다 크거나 같으므로 해당 물건 들어올 수 있음
            # 새로운 value를 넣는것이므로 이전물건일때 최대값 무게를 찾아줘야함
            # j - weight: 어떠한 ?의 무게 더하기 weight이 j값이 되야(w+?=j) (j는 최대가방의크기라 생각)
            # 해당 조건문안에 들어오게됨(즉 dp[i-1][?])
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
print(dp[N][K])
