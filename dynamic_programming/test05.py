test = int(input())

s = [list(map(int,input().split())) for i in range(test)]
# print(s)
for i in range(1,len(s)):
    s[i][0] = s[i][0] + min(s[i-1][1],s[i-1][2]) # 빨강
    s[i][1] = s[i][1] + min(s[i-1][0],s[i-1][2]) # 초록
    s[i][2] = s[i][2] + min(s[i-1][0],s[i-1][1]) # 파랑
# print(s)
print(min(s[test-1][0],s[test-1][1],s[test-1][2]))    
