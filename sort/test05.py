n = input()
result = []
for i in n:
    result.append(int(i))
result.sort(reverse=True)

answer = ""
for i in result:
    answer += str(i)
print(answer)    
