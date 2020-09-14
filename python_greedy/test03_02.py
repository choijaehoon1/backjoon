# 그리디 제일 욕심적인 해를 구하는 것(탐욕적)
# 어떻게 해야 최고로 욕심적으로 풀 수 있을까?
n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

answer = 0
min_value = 0
for i in arr:
    min_value = min(i)
    answer = max(min_value,answer)
print(answer)    
