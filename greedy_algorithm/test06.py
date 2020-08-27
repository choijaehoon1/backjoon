time_list = [300, 60, 10]

n = int(input())

result = [0 for i in range(3)]

for i in range(3):
    result[i] = n//time_list[i]
    n %= time_list[i] 
if n != 0:
    print(-1)
else:
    print(*result)    

