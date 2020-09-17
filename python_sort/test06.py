n = int(input())

answer = []
for i in range(n):
    num = int(input())
    answer.append(num)
result = sorted(answer,reverse=True)    
print(*result)
