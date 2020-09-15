# 시간을 000000 문자 형태로 생각하여 풀이
cnt = 0
n = int(input())
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt+=1
print(cnt)                
