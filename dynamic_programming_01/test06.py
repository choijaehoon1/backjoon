n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
# print(s)
k = 2 # 시작은 2부터 해야함 1행에 2개의 값이 있으므로
for i in range(1, n):
    for j in range(k):
        if j == 0: # 맨 왼쪽 일때는 위에 값 더해주면 됨
            s[i][j] = s[i-1][j] + s[i][j]
        elif i == j: # 맨 오른쪽일때도 그위에 값 더해주면 됨
            s[i][j] = s[i-1][j-1] + s[i][j]
        else: # 왼쪽위 숫자와 오른쪽위 숫자를 비교해 큰 값을 더함
            s[i][j] = max(s[i-1][j-1],s[i-1][j])  + s[i][j]   
    k += 1    
print(max(s[n-1]))

