# 첫번째 입력받은 문자를 가지고 그다음 입력받은 문자를 비교할 것이므로 
# dp 2차원 배열 만들때 두번째 문자의 길이 +1만큼 리스트를 만들고
# 첫번째 문자의 길이 +1만큼 반복하여 생성함
# ex)  0 C A P C A K
#    0
#    A
#    C
#    A
#    Y
#    K
#    p
str01 = list(map(str, input())) # 행
str02 = list(map(str, input())) # 열
# 열을 만들어 놓고 * 행을 해야 행렬이됨
dp = [[0 for i in range(len(str02)+1)] for j in range(len(str01)+1)]
# print(dp)
# 처음 입력받은 문자를 기준으로 하여 비교 시작
for i in range(len(str01)):
    for j in range(len(str02)):
        if str01[i] == str02[j]:
            # 같은 값이 나오면 길이를 추가하겠다
            # 두 글자가 추가되기전 가장 큰길이에 +1(대각선 왼쪽)
            dp[i+1][j+1] = dp[i][j] +1
        else:
            # 지금까지 해왔던 값중 큰 값을 선택하겠다
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
# print(dp)            
print(dp[len(str01)][len(str02)])                
