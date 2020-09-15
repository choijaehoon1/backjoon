time_type = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
cnt = 0
n = int(input())
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if k in time_type or j in time_type or i in time_type :
                cnt+=1
print(cnt)                
