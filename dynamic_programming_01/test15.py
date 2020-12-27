n = int(input())
s = list(map(int, input().split()))
# print(s)
dp = [s[0]]

for i in range(len(s)-1):
    dp.append(max(dp[i]+s[i+1],s[i+1]))
# print(dp)    
print(max(dp))    
