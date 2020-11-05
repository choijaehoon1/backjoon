n = int(input())

line = 1

while n>line:
    n -= line
    line += 1

# print(line) # 몇번째 줄
# print(n) # 값
# 홀수번째 분자 내림차순, 분모 오름차순
if line%2 ==1:
    a = line - n +1 
    b = n
else:
    a = n
    b = line - n +1     
print(a,'/',b,sep='')    
